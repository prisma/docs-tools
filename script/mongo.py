from typing import Dict, Tuple
from pymongo import MongoClient

from stitched import stitched

client = MongoClient(
    "mongodb+srv://username:secretpass@migrationdata.1ptf869.mongodb.net/?retryWrites=true&w=majority"
)
db = client.data


def get_file_move_paths() -> dict[str, str]:
    entries = db.file_move_paths.find()
    return {entry["current"]: entry["new"] for entry in entries}


def get_file_surgery_paths() -> dict[str, Tuple[str, str | None]]:
    entries = db.file_surgery_paths.find()
    return {entry["current"]: (entry["new"], entry["redirect"] if "redirect" in entry.keys() else None) for entry in entries}


def get_file_delete_paths() -> Dict[str, str | None]:
    entries = db.file_delete_paths.find()
    return {entry["path"]:entry["redirect"] if "redirect" in entry.keys() else None for entry in entries}


def get_stitched_files(surgery_files: Dict[str, list[str]]) -> list[stitched]:
    entries = db.file_stitched_paths.find()
    tmp: list[stitched] = []
    for entry in entries:
        dest = entry["dest"]
        header = entry["header"]
        body = entry["body"]
        for i in body:
            i["key"] = db.file_surgery_paths.find({"_id": i["key"]})[0]["new"] ### get key from surgery file
            i = surgery_files[i["key"]][i["index"]]
        body = [surgery_files[i["key"]][i["index"]] for i in body]
        tmp.append(stitched(dest, header, body))
    return tmp
