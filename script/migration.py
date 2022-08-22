import os
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


# clear new directory
print("\nClearing new directory...")
shutil.rmtree(new_content_dir)
print("Done clearing new directory.\n")

# move files around
print("copying started...\n")

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
    print("from  {}\nto    {}".format(old, new))

for old, (new, redirect) in file_surgery_paths.items(): ### move files from old to surgery
    old = old_content_dir + old
    new = surgery_dir + new

    os.makedirs(os.path.dirname(new), exist_ok=True)
    shutil.copy(old, new)
    print("from  {}\nto    {}".format(old, new))

print("\nfinished copying")


# stitch together sugery files
print("stitching started...\n")

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

file_stitched: List[stitched] = get_stitched_files(surgery_files)

for i in file_stitched: i.construct(True)

print("\nfinished stitching")


# edit redirects
os.makedirs(os.path.dirname(new_vercel), exist_ok=True)
shutil.copy(old_vercel, new_vercel)

## add redirects from moves
redirects: Dict[str, str | None] = {}

## add redirects from delete
for path, redirect in file_move_paths.items():
    redirects[path] = redirect

## add redirects from surgery
for path, (_, redirect) in file_surgery_paths.items():
    redirects[path] = redirect

## add redirects from delete
for path, redirect in file_delete_paths.items():
    redirects[path] = redirect

## format redirects
tmp_redirects: dict[str, str | None] = {}
for path, redirect in redirects.items(): ### remove numbers in path
    tmp = []
    for path in [path, redirect] if redirect is not None else [path]:
        path = (" " + path).split("/")[1:] ### remove first '/' so '/docs' can be added without '/docs//...' issue
        ttmp = ["docs"]
        for dir in path:
            i = dir.split("-") ### split by '-' to find numbers
            try:
                int(i[0])
                ttmp.append("-".join(i[1:]))
            except:
                ttmp.append(dir)
        tmp.append("/".join(ttmp))
    tmp = ["/" + i[:-4] if i[-4:] == ".mdx" else "/" + i for i in tmp] ### remove '.mdx' from path and add '/' add the beginning
    
    if len(tmp) > 1: ### if there is a redirect
        if tmp[0] != tmp[1]:
            tmp_redirects[tmp[0]] = tmp[1]
    else: ### if there is no redirect
        tmp_redirects[tmp[0]] = None
   
#### <---- TODO: write redirects and 410s (need to figure out where to put them) ----> ####
 
## write redirects to vercel.json
#f = open(new_vercel, encoding="utf8")
#vercel = json.loads(f.read())
#f.close()


# clean up
print("\ncleaning up")
shutil.rmtree(surgery_dir)
print("finished cleaning up")
