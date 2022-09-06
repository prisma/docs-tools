from typing import Dict, List, Tuple
import requests

from stitched import stitched


def get_file_move_paths() -> dict[str, str]:
    response = requests.get("https://docs-tools.vercel.app/api/file_move_paths", headers={"Content-Type": "application/json"}, data=str({})).json()
    return {i["current_path"]: i["new_path"] for i in response}

def get_file_surgery_paths() -> dict[str, Tuple[str, str | None]]:
    response = requests.get("https://docs-tools.vercel.app/api/file_surgery_paths", headers={"Content-Type": "application/json"}, data=str({})).json()
    return {i["current_path"]: (i["new_path"], i["redirect"] if "redirect" in i.keys() else None) for i in response}

def get_file_delete_paths() -> Dict[str, str | None]:
    response = requests.get("https://docs-tools.vercel.app/api/file_delete_paths", headers={"Content-Type": "application/json"}, data=str({})).json()
    return {i["current_path"]:i["redirect"] if "redirect" in i.keys() else None for i in response}

def get_stitched_files(surgery_files: Dict[str, list[str]]) -> List[Dict]:
    response = requests.get("https://docs-tools.vercel.app/api/file_stitched_paths", headers={"Content-Type": "application/json"}, data=str({})).json()
    return [{
        "new_path": i["new_path"], 
        "header": i["header"], 
        "body": [surgery_files[
            j["key"]
        ][
            int(j["index"])
        ] for j in i["body"]]} for i in response]