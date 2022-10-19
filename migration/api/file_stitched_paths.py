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

    collection = "file_stitched_paths"
    if request.headers.get("database"):
        collection += "_"
        collection += request.headers.get("database")

    stitched_type = {
        "_id": [str, NoneType],
        "name": [str, NoneType],
        "new_path": [str],
        "header": [dict],
        "body": [list],
    }
    
    client = MongoClient(os.environ['MONGODB_URI'])
    if request.headers.get('Content-Type') != 'application/json': return Response("Content-Type must be application/json", mimetype='text/plain', status=400)
    body = request.json
    
    if request.method == 'PUT':
        response = []
        for i in body:
            try:
                client.data[collection].insert_one({key:[{key:client.data.file_surgery_paths.find_one({"new_path": value})["_id"] if key == "key" else value for key, value in item.items()} for item in value] if key == "body" else value for key, value in validate_type(i, stitched_type).items()})
                response.append("OK")
            except:
                response.append("ERR")
        client.data.changes.insert_one({})
        return Response(json.dumps(response), mimetype='application/json', status=200)
    
    elif request.method == 'GET':
        try:
            return Response(json.dumps([{key:str(value) if type(value) == ObjectId else [{"index": bodypart["index"], "key": client.data[collection].find_one({"_id": bodypart["key"]})["new_path"]} for bodypart in value] if key == "body" else value for key, value in item.items()} for item in list(client.data.file_stitched_paths.find(validate_query(body, stitched_type)))]), mimetype='application/json')
        except:
            return Response(json.dumps({"Error": "bad shape"}), mimetype='application/json')
        
    elif request.method == 'POST':
        data = [(validate_query(i["query"], stitched_type), i["update"]) for i in body]
        response = []
        for query, update in data:
            res = client.data[collection].update_many(query, update)
            response.append({"matched_count": res.matched_count, "modified_count": res.modified_count})
        return Response(json.dumps(response), mimetype='application/json')
    
    elif request.method == 'DELETE':
        data = client.data[collection].delete_many(validate_query({key:[{key:client.data.file_surgery_paths.find_one({"new_path": value})["_id"] if key == "key" else value for key, value in item.items()} for item in value] if key == "body" else value for key,value in body.items()}, stitched_type))
        client.data.changes.insert_one({})
        return Response(json.dumps({"deleted": data.deleted_count}), mimetype='application/json')
