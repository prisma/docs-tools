# Error messages script

This script autogenerates the [error reference page](https://www.prisma.io/docs/reference/api-reference/error-reference) from the error text in the code repos.

## Using the Script

### Prerequisites

- Python 3.x.x
- Pip

### Setup

- Install dependancies with `python3 -m pip install -r requirements.txt`

### Running the Script

- Run `python3 error_code_parser_v2.py`
- This prints the output text.
  - Copy the output into `content/400-reference/200-api-reference/250-error-reference.mdx`
  - Or pipe the output into a file with `python3 error_code_parser_v2.py > error_codes.md` and copy from the new `error_codes.md` file (UNIX)

### Editing the Script

- Format the script before committing with `python3 -m black ./error_code_parser_v2.py`
