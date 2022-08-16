import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        client = MongoClient(os.environ.get("MONGODB_URI"), server_api=ServerApi('1'), serverSelectionTimeoutMS=5000)
        entries = client.data.file_move_paths.find()
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(str({entry["current"]: entry["new"] for entry in entries}))
        return
        