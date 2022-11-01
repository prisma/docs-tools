## Error messages script

This script autogenerates the [error reference page](https://www.prisma.io/docs/reference/api-reference/error-reference) from the error text in the code repos.

To run it:

- Install the latest version of Python 3. (If you’re using [Homebrew](https://brew.sh/), you can do this with `brew install python`. Otherwise see instructions here.)
- Install the dependancies in `requirements.txt`. You can do this with `python3 -m pip -r requirements.txt` if you installed Python with Homebrew or otherwise have PIP installed. Other install methods are listed [here](https://docs.python-requests.org/en/latest/user/install/#install).
- Copy the [error_code_parser script](https://github.com/prisma/docs-tools/blob/main/error-messages/error_code_parser_v2.py) into a directory somewhere
- Inside that directory, run `python3 error_code_parser_v2.py`

This outputs the error text. Copy this error text into `content/400-reference/200-api-reference/250-error-reference.mdx`.
