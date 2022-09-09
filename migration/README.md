# [Migration Script](https://www.notion.so/prismaio/IA-migration-script-4e7caef78f8a45dd8f3b0a38a86484af)

This repository contains the source code for the Prisma Docs Migration Script, the supporting API, and the webform.

## How to Run

- setup you run environment
- go to the website to input data
- edit the content directory
- run the script

## Setup

- from [prisma/docs-tools](https://github.com/prisma/docs-tools) copy the contents `migration/script`
- from [prisma/docs](https://github.com/prisma/docs) clone `staging` into `./old` with `git clone --branch staging https://github.com/prisma/docs ./old`
- from [prisma/docs](https://github.com/prisma/docs) clone `main` into `./new` with `git clone https://github.com/prisma/docs ./new`

## Run the Script

- `python migration.py`
