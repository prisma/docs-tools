from http.server import BaseHTTPRequestHandler
import os
from pymongo import MongoClient
import json
from flask import Flask, Response
app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['PUT', 'GET', 'DELETE'])
@app.route('/<path:path>', methods=['PUT', 'GET', 'DELETE'])
def catch_all(path):
    from flask import request
    
    if request.method == 'PUT':
        if request.headers.get('Content-Type') != 'application/json': return Response("Content-Type must be application/json", mimetype='text/plain', status=400)
        body = request.json
        client = MongoClient(os.environ['MONGODB_URI'])
        data = [{
            "name": i["name"] if "name" in i.keys() else None,
            "dest": i["dest"],
            "header": i["header"],
            "body": [{
                "key": client.data.file_surgery_paths.find_one({"new": j["key"]})["_id"],
                "index": j["index"]
            } for j in i["body"]]
        } for i in body["data"]]
        client.data.file_stitched_paths.insert_many([{j:i[j] for j in i.keys() if i[j] != None} for i in data])
        return Response("OK")
    
    elif request.method == 'GET':
        if request.headers.get('Content-Type') != 'application/json': return Response("Content-Type must be application/json", mimetype='text/plain', status=400)
        body = request.json
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
    
    elif request.method == 'DELETE':
        if request.headers.get('Content-Type') != 'application/json': return Response("Content-Type must be application/json", mimetype='text/plain', status=400)
        body = request.json
        args = {}
        if "_id" in body.keys():
            args["_id"] = body["_id"]
        if "name" in body.keys():
            args["name"] = body["name"]
        if "dest" in body.keys():
            args["dest"] = body["dest"]
        if "header" in body.keys():
            args["header"] = body["header"]
        if "body" in body.keys():
            args["body"] = body["body"]
        client = MongoClient(os.environ['MONGODB_URI'])
        data = client.data.file_stitched_paths.delete_many(args)
        
        return Response(json.dumps({"deleted": data.deleted_count}), mimetype='application/json')
