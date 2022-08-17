from typing import Dict, Tuple
import requests

from stitched import stitched


def get_file_move_paths() -> dict[str, str]:
    response = requests.get("https://migration-script.vercel.app/api/file_move_paths", headers={"Content-Type": "application/json"}, data=str({})).json()
    return {i["current"]: i["new"] for i in response}

def get_file_surgery_paths() -> dict[str, Tuple[str, str | None]]:
    response = requests.get("https://migration-script.vercel.app/api/file_surgery_paths", headers={"Content-Type": "application/json"}, data=str({})).json()
    return {i["current"]: (i["new"], i["redirect"] if "redirect" in i.keys() else None) for i in response}

def get_file_delete_paths() -> Dict[str, str | None]:
    response = requests.get("https://migration-script.vercel.app/api/file_delete_paths", headers={"Content-Type": "application/json"}, data=str({})).json()
    return {i["path"]:i["redirect"] if "redirect" in i.keys() else None for i in response}

def get_stitched_files(surgery_files: Dict[str, list[str]]) -> list[stitched]:
    response = requests.get("https://migration-script.vercel.app/api/file_stitched_paths", headers={"Content-Type": "application/json"}, data=str({})).json()
    return [stitched(
        i["dest"], 
        i["header"], 
        [surgery_files[
            j["key"]
        ][
            int(j["index"])
        ] for j in i["body"]]) for i in response]