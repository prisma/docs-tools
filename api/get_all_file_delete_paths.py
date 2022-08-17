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
            "path": i["path"],
            "redirect": i["redirect"] if "redirect" in i.keys() else None
            } for i in client.data.file_delete_paths.find()]
        self.wfile.write(json.dumps([{j:i[j] for j in i.keys() if i[j] != None} for i in data]).encode())
        return