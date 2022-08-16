import os
from pymongo import MongoClient

from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        client = MongoClient(os.environ.get("MONGODB_URI"))
        return
        