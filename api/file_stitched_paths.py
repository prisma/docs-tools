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

    stitched_type = {
        "_id": [str, None],
        "name": [str, None],
        "new_path": [str],
        "header": [dict],
        "body": [list],
    }
    
    client = MongoClient(os.environ['MONGODB_URI'])
    
    if request.headers.get('Content-Type') != 'application/json': return Response("Content-Type must be application/json", mimetype='text/plain', status=400)
    body = request.json
    
    if request.method == 'PUT':
        if request.headers.get('Content-Type') != 'application/json': return Response("Content-Type must be application/json", mimetype='text/plain', status=400)
        body = request.json
        response = []
        def format(i):
            try:
                formated = {
                    "name": i["name"] if "name" in i.keys() else None,
                    "dest": i["dest"],
                    "header": i["header"],
                    "body": [{
                        "key": client.data.file_surgery_paths.find_one({"new": j["key"]})["_id"],
                        "index": j["index"]
                    } for j in i["body"]]
                }
                response.append("OK")
                return formated
            except:
                response.append("ERR")
                return None
        data = [j for j in [format(i) for i in body["data"]] if j != None] 
        client.data.file_stitched_paths.insert_many([{j:i[j] for j in i.keys() if i[j] != None} for i in data])
        client.data.changes.insert_one({})
        return Response(json.dumps(response), mimetype='application/json', status=200)
    
    elif request.method == 'GET':
        try:
            return Response(json.dumps([{key:str(value) if type(value) is ObjectId else [{"index": bodypart["index"], "key": client.data.file_surgery_paths.find_one(bodypart["key"])["new"]} for bodypart in value] if key is body else value for key, value in item.items()} for item in list(client.data.file_stitched_paths.find(validate_query(body, stitched_type)))]), mimetype='application/json')
        except:
            return Response(json.dumps({"Error": "bad shape"}), mimetype='application/json')
    
    elif request.method == 'DELETE':
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
        data = client.data.file_stitched_paths.delete_many(args)
        client.data.changes.insert_one({})
        return Response(json.dumps({"deleted": data.deleted_count}), mimetype='application/json')
