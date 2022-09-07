# Gets all .mdx file paths in the contents directory of the docs repo
# and prints them to standard output
# Usage: python3 get_urls.py <path-to-contents-directory>

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
    f2 = "/" + f
    print(f2)
