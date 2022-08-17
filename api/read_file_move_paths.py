from http.server import BaseHTTPRequestHandler
import os
from pymongo import MongoClient
import json
from flask import Flask, Response
app = Flask(__name__)

@app.route('/read/file_move_paths')
def catch_all():
    args = {}
    #if "_id" in self.headers.keys():
    #    args["_id"] = self.headers["_id"]
    #if "name" in self.headers.keys():
    #    args["name"] = self.headers["name"]
    #if "current" in self.headers.keys():
    #    args["current"] = self.headers["current"]
    #if "new" in self.headers.keys():
    #    args["new"] = self.headers["new"]
    client = MongoClient(os.environ['MONGODB_URI'])
    data = [{
        "_id": str(i["_id"]),
        "name": i["name"] if "name" in i.keys() else None,
        "current": i["current"],
        "new": i["new"]
        } for i in client.data.file_move_paths.find(args)]

    return Response(json.dumps([{j:i[j] for j in i.keys() if i[j] != None} for i in data]), mimetype='application/json')
