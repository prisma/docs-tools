## Error messages script

This script is sued to autogenerate the [Error Reference page](http://localhost:8000/reference/api-reference/error-reference) from the error text in the code repos.

To run it:

- Install the latest version of Python 3. (If you’re using [Homebrew](https://brew.sh/), you can do this with `brew install python`. Otherwise see instructions here.)
- Install the `requests` dependency. You can do this with `python3 -m pip install requests` if you installed Python with Homebrew or otherwise have PIP installed. Other install methods are listed [here](https://docs.python-requests.org/en/latest/user/install/#install).
- Copy the [error_code_parser script](https://github.com/prisma/docs-tools/blob/main/error-messages/error_code_parser.py) into a directory somewhere
- Inside that directory, run `python3 error_code_parser.py`

This will output the error text to copy into `content/400-reference/250-error-reference.mdx`
