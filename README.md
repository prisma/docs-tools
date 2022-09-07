# Docs Tools

This repository is for tools that the Docs teams uses for various tasks:

- migration script: this script, with an accompanying front-end webform on Vercel and a MongoDB Atlas DB, will be used to auto-build the new structure for the docs, as part of the Information Architecture effort.
- script for generating docs for the error messages (thanks to @mhwelander for the initial script!)
- set up script to automatically set up a new Prisma project for testing purposes
- docs URLs scripts to get the filepaths of Prisma docs files and their corresponding URLs

## Migration script

The migration script is a python script that will restucture all of our docs at once so we don't have to handle pull requests not being able to be mergeed while working on the docs restucture. This repo also includes a webform and an API for taking in data for the script to use.

## Error message docs generation script

The error messages script auto-generates the reference documentation for all Prisma errors.

## Set up script

This is a bash script to automatically set up a new Prisma project for testing purposes, using the steps in the Getting Started guides.

## Docs URLs script

This contains two Python scripts to get the filepaths of Prisma docs files and their corresponding URLs.
