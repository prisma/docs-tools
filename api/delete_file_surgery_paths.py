from http.server import BaseHTTPRequestHandler
import os
from pymongo import MongoClient
import json
from flask import Flask, Response
app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['DELETE'])
@app.route('/<path:path>', methods=['DELETE'])
def catch_all(path):
    from flask import request
    if request.headers.get('Content-Type') != 'application/json': return Response("Content-Type must be application/json", mimetype='text/plain', status=400)
    body = request.json
    args = {}
    if "_id" in body.keys():
        args["_id"] = body["_id"]
    if "name" in body.keys():
        args["name"] = body["name"]
    if "current" in body.keys():
        args["current"] = body["current"]
    if "new" in body.keys():
        args["new"] = body["new"]
    if "redirect" in body.keys():
        args["redirect"] = body["redirect"]
    client = MongoClient(os.environ['MONGODB_URI'])
    data = client.data.file_surgery_paths.delete_many(args)
    
    return Response(json.dumps({"deleted": data.deleted_count}), mimetype='application/json')
