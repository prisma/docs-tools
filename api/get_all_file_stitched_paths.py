from http.server import BaseHTTPRequestHandler
import os
from pymongo import MongoClient
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        client = MongoClient(os.environ['MONGODB_URI'])
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        data = [{
            "name": i["name"] if "name" in i.keys() else None,
            "dest": i["dest"],
            "header": i["header"],
            "body": [{
                "key": client.data.file_surgery_paths.find_one({"_id": j["key"]})["new"],
                "index": j["index"]
                } for j in i["body"]]
            } for i in client.data.file_stitched_paths.find()]
        for i in data:
            for x, y in i.items():
                if y == None:
                    del i[x]
        self.wfile.write(json.dumps(data).encode())
        return
