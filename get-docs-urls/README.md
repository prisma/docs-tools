This directory contains two Python scripts:

- `get_urls.py` gets all .mdx file paths in the `content` directory of the docs repo, converts them to their corresponding URLs, and prints them to standard output
- `get_filepaths.py` gets all .mdx file paths in the `content` directory of the docs repo and just prints them to standard output. Maybe having this as a script is overkill given that you can also just run `find . -type f -name "*.mdx"` in the terminal, but it was an easy way to print them in the same order as in the `get_urls.py` script!

## Getting Prisma docs URLS

To run it, navigate to the `get-docs-urls` directory and run:

```
python3 get_urls.py <path-to-content-directory>
```

where `<path-to-content-directory>` is the path to the `content` directory of your docs repo.

## Getting Prisma docs filepaths

To run it, navigate to the `get-docs-urls` directory and run:

```
python3 get_filepaths.py <path-to-content-directory>
```

where `<path-to-content-directory>` is the path to the `content` directory of your docs repo.
