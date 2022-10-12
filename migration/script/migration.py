import os
import re
import shutil
from typing import Dict, List, Tuple

from api import (
    get_file_move_paths,
    get_file_surgery_paths,
    get_file_delete_paths,
    get_stitched_files,
)

from stitched import stitched
from const import *

file_move_paths: Dict[str, str] = get_file_move_paths()
file_surgery_paths: Dict[str, Tuple[str, str | None]] = get_file_surgery_paths()
file_delete_paths: Dict[str, str | None] = get_file_delete_paths()



print("\033[0;36mClearing new directory...\033[0m")

# clear new directory
shutil.rmtree(new_content_dir)

print("\033[0;36mDone clearing new directory\033[0m")



print()



print("\033[0;36mCopying started...\033[0m")

# move files around

## add all unmoved files as their current directory
for root, dirs, files in os.walk(old_content_dir):
    for file in files:
        path = os.path.join(root, file)[len(old_content_dir) :].replace("\\", "/")

        if (
            file_move_paths.get(path) is None
            and file_surgery_paths.get(path) is None
            and file_delete_paths.get(path) is None
        ):
            file_move_paths[path] = path

## move files
for old, new in file_move_paths.items(): ### move files from old to new
    old = old_content_dir + old
    new = new_content_dir + new

    os.makedirs(os.path.dirname(new), exist_ok=True)
    shutil.copy(old, new)
    print("\033[0;32mfrom\033[0m  {}\n\033[0;32mto\033[0m    {}".format(old, new))

for old, (new, redirect) in file_surgery_paths.items(): ### move files from old to surgery
    old = old_content_dir + old
    new = surgery_dir + new

    os.makedirs(os.path.dirname(new), exist_ok=True)
    shutil.copy(old, new)
    print("\033[0;32mfrom\033[0m  {}\n\033[0;32mto\033[0m    {}".format(old, new))

print("\033[0;36mFinished copying\033[0m")



print()



print("\033[0;36mStitching started...\033[0m")

# stitch together surgery files
## make sure surgery directory exists
os.makedirs(surgery_dir, exist_ok=True) 

## cut up old files
surgery_files: Dict[str, list[str]] = {}

for root, dirs, files in os.walk(surgery_dir): ### walk through surgery directory
    for file in files:
        path = os.path.join(root, file)[len(surgery_dir) :].replace("\\", "/")
        f = open(surgery_dir + path, "r", encoding="utf8")
        surgery_files[path] = "".join(f.read().split("---")[2:]).split(separation_string)
        f.close()

file_stitched_paths = get_stitched_files(surgery_files)

file_stitched: List[stitched] = [stitched(i["new_path"], i["header"], i["body"]) for i in file_stitched_paths]

for i in file_stitched:
    i.construct()
    print("\033[0;32mstitching\033[0m {}".format(i.dest))

print("\033[0;36mFinished stitching\033[0m")



print()



print("\033[0;36mAdding redirects...\033[0m")

# edit redirects
os.makedirs(os.path.dirname(new_vercel), exist_ok=True)
shutil.copy(old_vercel, new_vercel)

## add redirects from moves
redirects: Dict[str, str] = {}
deletes: List[str] = []

for old, new in file_move_paths.items():
    if old != new:
        redirects[old] = new

for old, (new, redirect) in file_surgery_paths.items():
    if redirect == None:
        deletes.append(old)
    else:
        redirects[old] = redirect
        
for old, redirect in file_delete_paths.items():
    if redirect == None:
        deletes.append(old)
    else:
        redirects[old] = redirect
    
def format_redirect(redirect: str) -> str:
    tmp = [i.split("-") for i in redirect.split("/")]
    tmp = [i for i in tmp if len(i) > 1]
    
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            if tmp[i][j] == "":
                del tmp[i][j]
    for i in range(len(tmp)):
        if bool(re.search("^\d+$", tmp[i][0])):
            del tmp[i][0]
        if bool(re.search(".mdx$", tmp[i][-1])):
            tmp[i][-1] = tmp[i][-1][:-4]
        if bool(re.search("^index$", tmp[i][-1])):
            del tmp[i][-1]
    return "/" + "/".join(["-".join(i) for i in tmp])

redirects = {format_redirect(i):format_redirect(j) for i, j in redirects.items()}
deletes = [format_redirect(i) for i in deletes if i not in redirects.keys()]

redirects = {i:j for i, j in redirects.items() if i not in [format_redirect(i) for i in file_move_paths.values()] and i not in [i["new_path"] for i in file_stitched_paths]}
deletes = [i for i in deletes if i not in [format_redirect(i) for i in file_move_paths.values()] and i not in [i["new_path"] for i in file_stitched_paths]]

## add redirects and deletes to vercel.json
redirect_file = {}
with open(new_vercel, 'r') as f:
    redirect_file = json.loads(f.read())

for i, j in redirects.items():
    redirect_file["redirects"].append({"source": i, "destination": j})
    
for i in deletes:
    redirect_file["redirects"].append({"source": i, "destination": "/410", "statusCode": 410})

with open(new_vercel, 'w') as f:
    f.write(json.dumps(redirect_file, indent=4))

print("\033[0;36mAdded redirects\033[0m")



print()



print("\033[0;36mFixing broken links...\033[0m")

# Fix broken links
for root, dirs, files in os.walk(new_content_dir): 
    for file in files:
        path = os.path.join(root, file)[len(new_content_dir) :].replace("\\", "/")
        if path[-4:] == ".mdx":
            with open(new_content_dir + path, "r", encoding="utf8") as f:
                filedata = f.read()
            newfiledata = filedata
            for old, new in redirects.items():
                newfiledata = newfiledata.replace("(" + old + ")", "(" + new + ")").replace("(" + old + "#", "(" + new + "#")
                if newfiledata != filedata:
                    print("\033[0;32mfixed links in\033[0m " + path + "\n\033[0;32mreplaced\033[0m       " + old + "\n\033[0;32mwith\033[0m           " + new)
            f = open(new_content_dir + path, "w", encoding="utf8")
            f.write(newfiledata)
            f.close()

print("\033[0;36mFixed broken links\033[0m")



print()



print("\033[0;36mCleaning up...\033[0m")

# clean up
shutil.rmtree(surgery_dir)

print("\033[0;36mFinished cleaning up\033[0m")
