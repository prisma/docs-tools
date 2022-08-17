from http.server import BaseHTTPRequestHandler
import os
from pymongo import MongoClient

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        import os
        from pymongo import MongoClient
        client = MongoClient(os.environ['MONGODB_URI'])
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write([{
            "name": i["name"],
            "dest": i["dest"],
            "header": i["header"],
            "body": [{
                "key": client.data.file_surgery_paths.find_one({"_id": j["key"]})["new"],
                "index": j["index"]
                } for j in i["body"]]
            } for i in client.data.file_stitched_paths.find()])
        return
