# This script is for generating error codes for the documentation
# pyproject.toml holds the config for black
import re
import requests

ERROR_FILES = [
    ("https://raw.githubusercontent.com/prisma/prisma-engines/master/libs/user-facing-errors/src/common.rs", "Common"),
    ("https://raw.githubusercontent.com/prisma/prisma-engines/master/libs/user-facing-errors/src/query_engine.rs", "Prisma Client (Query Engine)"),
    ("https://raw.githubusercontent.com/prisma/prisma-engines/master/libs/user-facing-errors/src/migration_engine.rs", "Prisma Migrate (Migration Engine)"),
    ("https://raw.githubusercontent.com/prisma/prisma-engines/master/libs/user-facing-errors/src/introspection_engine.rs", "`prisma db pull` (Introspection Engine)"),
]
FORMAT_REPLACE_LIST = [
    (r"\\n", r"\n"),
    (r"\\t", r"\t"),
    (r"\\\\", r"\\"),
    (r'"\\\n', r'"'),
    (r'\n"\n', r'"\n'),
    ("\n\s*code =", "\ncode ="),
    ("\n\s*message =", "\nmessage ="),
    ("\#\[user_facing\(code =", "#[user_facing(\ncode ="),
    (", message =", ",\nmessage ="),
    ('"\)\]', '"\n)]'),
]

for url, title in ERROR_FILES:
    print("\n## ", title)
    # Get contents of the file file
    content = str(requests.get(url, allow_redirects=True).content)
    # Format content
    for before, after in FORMAT_REPLACE_LIST:
        content = re.sub(before, after, content)
    # Print code and message lines and format them into markdown
    content = iter(content.splitlines())
    for line in content:
        # If line is a code line, format into markdown and print
        if line.startswith("code ="):
            print(re.sub(r'code = "(.*?)",', r"\n### `\1`\n", line))
        # If line is a message line, format into markdown and print
        if line.startswith("message ="):
            line = re.sub(r'message = "(.*?)', r"\1", line)
            print(line[:-1] if line.endswith('"') else line)
            # If this line is not the end on the message then continue printing lines until the end of the string is found
            while not line.endswith('"'):
                line = content.__next__()
                print(line[:-1] if line.endswith('"') else line)
