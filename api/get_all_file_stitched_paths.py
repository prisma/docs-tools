from http.server import BaseHTTPRequestHandler
import os
from pymongo import MongoClient
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        args = {}
        if "_id" in self.headers.keys():
            args["_id"] = self.headers["_id"]
        if "name" in self.headers.keys():
            args["name"] = self.headers["name"]
        if "dest" in self.headers.keys():
            args["dest"] = self.headers["dest"]
        if "header" in self.headers.keys():
            args["header"] = self.headers["header"]
        if "body" in self.headers.keys():
            args["body"] = self.headers["body"]
        client = MongoClient(os.environ['MONGODB_URI'])
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        data = [{
            "_id": str(i["_id"]),
            "name": i["name"] if "name" in i.keys() else None,
            "dest": i["dest"],
            "header": i["header"],
            "body": [{
                "key": client.data.file_surgery_paths.find_one({"_id": j["key"]})["new"],
                "index": j["index"]
                } for j in i["body"]]
            } for i in client.data.file_stitched_paths.find(args)]
        self.wfile.write(json.dumps([{j:i[j] for j in i.keys() if i[j] != None} for i in data]).encode())
        return
