from http.server import BaseHTTPRequestHandler
import os
from pymongo import MongoClient
import json
from flask import Flask, Response
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    from flask import request
    body = request.json if type(request.json) is dict else {}
    args = {}
    if "_id" in body.keys():
        args["_id"] = body["_id"]
    if "name" in body.keys():
        args["name"] = body["name"]
    if "dest" in body.keys():
        args["dest"] = body["dest"]
    client = MongoClient(os.environ['MONGODB_URI'])
    data = [{
        "_id": str(i["_id"]),
        "name": i["name"] if "name" in i.keys() else None,
        "dest": i["dest"],
        "header": i["header"],
        "body": [{
            "key": client.data.file_surgery_paths.find_one({"_id": j["key"]})["new"],
            "index": j["index"]
            } for j in i["body"]]
        } for i in client.data.file_stitched_paths.find(args)]

    return Response(json.dumps([{j:i[j] for j in i.keys() if i[j] != None} for i in data]), mimetype='application/json')


