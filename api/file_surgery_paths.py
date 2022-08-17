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
    data = [{
        "name": i["name"] if "name" in i.keys() else None,
        "new": i["new"],
        "curret": i["current"],
        "redirect": i["redirect"] if "redirect" in i.keys() else None
    } for i in body["data"]]
    MongoClient(os.environ['MONGODB_URI']).data.file_surgery_paths.insert_many([{j:i[j] for j in i.keys() if i[j] != None} for i in data])
    return Response("OK")


@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>', methods=['GET'])
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
    data = [{
        "_id": str(i["_id"]),
        "name": i["name"] if "name" in i.keys() else None,
        "current": i["current"],
        "new": i["new"],
        "redirect": i["redirect"] if "redirect" in i.keys() else None
        } for i in client.data.file_surgery_paths.find(args)]
    return Response(json.dumps([{j:i[j] for j in i.keys() if i[j] != None} for i in data]), mimetype='application/json')


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
