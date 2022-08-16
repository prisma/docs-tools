import os
from typing import Any, Dict, List

from const import *


class stitched:
    header: Dict[str, Any]
    substrings: List[str]
    dest: str

    def __init__(
        self,
        dest: str,
        header: Dict[str, Any] = {},
        body: List[str] = [],
    ):
        self.header = header
        self.body = body
        self.dest = dest

    def construct(self, v=False):
        if v: print("stitching {}".format(self.dest))
        os.makedirs(
            os.path.dirname(new_content_dir + self.dest), exist_ok=True
        )
        f = open(new_content_dir + self.dest, "w", encoding="utf8")
        f.write(
            "---\n"
            + "\n".join([i + ": " + str(self.header[i]) for i in self.header])
            + "\n---"
            + "".join(self.body)
        )
        f.close()
