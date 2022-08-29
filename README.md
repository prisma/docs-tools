# Docs Tools

This repository is for tools that the Docs teams uses for various tasks:

* migration script: this script, with an accompanying front-end webform on Vercel and a MongoDB Atlas DB, will be used to auto-build the new structure for the docs, as part of the  Information Architecture effort.
* script for generating docs for the error messages (thanks to @mhwelander for the initial script!)
* ?


## Migration Script

The migration script is a python script that will restucture all of our docs at once so we don't have to handle pull requests not being able to be mergeed while working on the docs restucture. This repo also includes a webform and an API for taking in data for the script to use.
