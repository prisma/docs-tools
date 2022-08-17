from http.server import BaseHTTPRequestHandler
import os
from pymongo import MongoClient

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        import os
        from pymongo import MongoClient
        client = MongoClient(os.environ['MONGODB_URI'])
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write("testing 123".encode())
        return
