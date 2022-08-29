import json
from typing import Tuple
def config() -> Tuple[str, str, str, str, str, str]:
    with open("./config.json", "r") as f:
        config = json.loads(f.read())
    return (config["old_content_dir"], config["new_content_dir"], config["surgery_dir"], config["old_vercel"], config["new_vercel"], config["separation_string"])
old_content_dir, new_content_dir, surgery_dir, old_vercel, new_vercel, separation_string = config()
