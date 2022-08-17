from http.server import BaseHTTPRequestHandler
import os
from pymongo import MongoClient
import json
from flask import Flask, Response
app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['PUT'])
@app.route('/<path:path>', methods=['PUT'])
def catch_all(path):
    from flask import request
    if request.headers.get('Content-Type') != 'application/json': return Response("Content-Type must be application/json", mimetype='text/plain', status=400)
    body = request.json
    client = MongoClient(os.environ['MONGODB_URI'])
    data = [{
        "name": i["name"] if "name" in i.keys() else None,
        "dest": i["dest"],
        "header": i["header"],
        "body": [{"key": client.data.file_surgery_paths.find_one({"new": i["body"][j]["key"]})["_id"], "index": i["body"][j]["index"]} for j in i["body"]]
    } for i in body["data"]]
    client.data.file_surgery_paths.insert_many([{j:i[j] for j in i.keys() if i[j] != None} for i in data])
    return Response("OK")
