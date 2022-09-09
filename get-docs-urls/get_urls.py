# Gets all .mdx file paths in the contents directory of the docs repo,
# converts them to their corresponding URLs, and prints them to standard output
# Usage: python3 get_urls.py <path_to_contents directory>

import sys
import re
import os

mypath = sys.argv[1]

# Get all .mdx files in subdirectories (https://stackoverflow.com/a/13617120)
mdx_files = []
for dirpath, dirnames, files in os.walk(mypath):
    for file_name in files:
        rel_dir = os.path.relpath(dirpath, mypath)
        rel_file = os.path.join(rel_dir, file_name)
        if(os.path.splitext(rel_file)[1] == '.mdx'):
            mdx_files.append(rel_file)

# Convert to URLs
for f in mdx_files:
    f2 = "prisma.io/docs/" + f  # add domain
    f3 = f2[:len(f2) - 4]  # remove '.mdx' (strip last 4 characters)
    # # remove ordering numbers (replace "/<digits>-" with "/")
    f4 = re.sub(r'\/\d+-', '/', f3)
    f5 = re.sub(r'\/index$', '', f4)  # remove "/index" for contents pages

    print(f5)
