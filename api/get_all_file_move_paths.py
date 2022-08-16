import os
from pymongo import MongoClient

from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        client = MongoClient(os.environ.get("MONGODB_URI"))
        entries = client.data.file_move_paths.find()
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(str({entry["current"]: entry["new"] for entry in entries}))
        return
        