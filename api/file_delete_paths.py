from http.server import BaseHTTPRequestHandler
import os
from pymongo import MongoClient
from bson import ObjectId
import json
from flask import Flask, Response
from api._util.validate import *
app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['PUT', 'POST', 'GET', 'DELETE'])
@app.route('/<path:path>', methods=['PUT', 'POST', 'GET', 'DELETE'])
def catch_all(path):
    from flask import request

    delete_type = {
        "_id": [str, NoneType],
        "name": [str, NoneType],
        "current_path": [str],
        "redirect": [str, NoneType],
    }
    
    client = MongoClient(os.environ['MONGODB_URI'])
    if request.headers.get('Content-Type') != 'application/json': return Response("Content-Type must be application/json", mimetype='text/plain', status=400)
    body = request.json
    
    if request.method == 'PUT':
        response = []
        for i in body:
            try:
                client.data.file_delete_paths.insert_one(validate_type(i, delete_type))
                response.append("OK")
            except:
                response.append("ERR")
        client.data.changes.insert_one({})
        return Response(json.dumps(response), mimetype='application/json', status=200)
    
    elif request.method == 'GET':
        try:
            return Response(json.dumps([{key:str(value) if type(value) is ObjectId else value for key, value in item.items()} for item in list(client.data.file_delete_paths.find(validate_query(body, delete_type)))]), mimetype='application/json')
        except:
            return Response(json.dumps({"Error": "bad shape"}), mimetype='application/json')
    
    elif request.method == 'POST':
        data = [(i["query"], i["update"]) for i in body]
        return Response(json.dumps(data), mimetype='application/json')

    elif request.method == 'DELETE':
        args = {}
        if "_id" in body.keys():
            args["_id"] = body["_id"]
        if "name" in body.keys():
            args["name"] = body["name"]
        if "path" in body.keys():
            args["path"] = body["path"]
        if "redirect" in body.keys():
            args["redirect"] = body["redirect"]
        data = client.data.file_delete_paths.delete_many(args)
        client.data.changes.insert_one({})
        return Response(json.dumps({"deleted": data.deleted_count}), mimetype='application/json')
