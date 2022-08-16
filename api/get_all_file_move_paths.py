from pymongo import MongoClient

from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        client = MongoClient(
            "mongodb+srv://username:secretpass@migrationdata.1ptf869.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1')
        )
        entries = client.data.file_move_paths.find()
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(str(entries))
        return
        