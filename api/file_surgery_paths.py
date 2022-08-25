from http.server import BaseHTTPRequestHandler
import os
from types import NoneType
from pymongo import MongoClient
from bson import ObjectId
import json
from flask import Flask, Response
from api._util.validate import *
app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['PUT', 'GET', 'DELETE'])
@app.route('/<path:path>', methods=['PUT', 'GET', 'DELETE'])
def catch_all(path):
    from flask import request

    surgery_type = {
        "_id": [str, NoneType],
        "name": [str, NoneType],
        "current_path": [str],
        "new_path": [str],
        "redirect": [str, NoneType],
    }
    
    client = MongoClient(os.environ['MONGODB_URI'])
    
    if request.headers.get('Content-Type') != 'application/json': return Response("Content-Type must be application/json", mimetype='text/plain', status=400)
    body = request.json
    
    if request.method == 'PUT':
        response = []
        def format(i):
            try:
                formated = {
            "name": i["name"] if "name" in i.keys() else None,
            "new": i["new"],
            "current": i["current"],
            "redirect": i["redirect"] if "redirect" in i.keys() else None
        }
                response.append("OK")
                return formated
            except:
                response.append("ERR")
                return None
        data = [j for j in [format(i) for i in body["data"]] if j != None]
        client.data.file_surgery_paths.insert_many([{j:i[j] for j in i.keys() if i[j] != None} for i in data])
        client.data.changes.insert_one({})
        return Response(json.dumps(response), mimetype='application/json', status=200)
    
    elif request.method == 'GET':
        try:
            return Response(json.dumps([{key:str(value) if type(value) is ObjectId else value for key, value in item.items()} for item in list(client.data.file_surgery_paths.find(validate_query(body, surgery_type)))]), mimetype='application/json')
        except:
            return Response(json.dumps({"Error": "bad shape"}), mimetype='application/json')
    
    elif request.method == 'DELETE':
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
        data = client.data.file_surgery_paths.delete_many(args)
        client.data.changes.insert_one({})
        return Response(json.dumps({"deleted": data.deleted_count}), mimetype='application/json')
