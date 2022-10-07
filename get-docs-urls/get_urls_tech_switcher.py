# Generates all tech switcher URLs for the getting started pages
# Usage: python3 get_urls_tech_switcher.py <path_to_contents directory>

import sys
import re
import os

mypath = sys.argv[1]

# Start of URLs for pages using the tech switcher
scratch_relational = "prisma.io/docs/getting-started/setup-prisma/start-from-scratch/relational-databases"
scratch_mongodb = "prisma.io/docs/getting-started/setup-prisma/start-from-scratch/mongodb"
existing_relational = "prisma.io/docs/getting-started/setup-prisma/add-to-existing-project/relational-databases"
existing_mongodb = "prisma.io/docs/getting-started/setup-prisma/add-to-existing-project/mongodb"

# Generate URL variants for relational database getting started guides


def print_urls_relational(url):
    print(url + "-typescript-mysql")
    print(url + "-typescript-postgres")
    print(url + "-typescript-sqlserver")
    print(url + "-typescript-planetscale")
    print(url + "-typescript-cockroachdb")
    print(url + "-node-mysql")
    print(url + "-node-postgres")
    print(url + "-node-sqlserver")
    print(url + "-node-planetscale")
    print(url + "-node-cockroachdb")

# Generate URL variants for MongoDB getting started guides


def print_urls_mongodb(url):
    print(url + "-typescript-mongodb")
    print(url + "-node-mongodb")


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
    url = re.sub(r'\/index$', '', f4)  # remove "/index" for contents pages

    # print
    if (scratch_relational in url):
        print_urls_relational(url)
    if (existing_relational in url):
        print_urls_relational(url)
    if (scratch_mongodb in url):
        print_urls_mongodb(url)
    if (existing_mongodb in url):
        print_urls_mongodb(url)
