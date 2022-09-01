import json
from typing import Tuple
def config() -> Tuple[str, str, str, str]:
    with open("./config.json", "r") as f:
        config = json.loads(f.read())
    return (config["old_dir"], config["new_dir"], config["surgery_dir"], config["separation_string"])
old_dir, new_dir, surgery_dir, separation_string = config()
old_content_dir = old_dir + "/content"
new_content_dir = new_dir + "/content"
old_gatsby_node = old_dir + "/gatsby-node.js"
new_gatsby_node = new_dir + "/gatsby-node.js"
old_vercel = old_dir + "/vercel.json"
new_vercel = new_dir + "/vercel.json"