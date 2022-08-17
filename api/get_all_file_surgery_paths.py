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
        if "current" in self.headers.keys():
            args["current"] = self.headers["current"]
        if "new" in self.headers.keys():
            args["new"] = self.headers["new"]
        if "redirect" in self.headers.keys():
            args["redirect"] = self.headers["redirect"]
        client = MongoClient(os.environ['MONGODB_URI'])
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        data = [{
            "_id": i["_id"],
            "name": i["name"] if "name" in i.keys() else None,
            "current": i["current"],
            "new": i["new"],
            "redirect": i["redirect"] if "redirect" in i.keys(args) else None
            } for i in client.data.file_surgery_paths.find()]
        self.wfile.write(json.dumps([{j:i[j] for j in i.keys() if i[j] != None} for i in data]).encode())
        return