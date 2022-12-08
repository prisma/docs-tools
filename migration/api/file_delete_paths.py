from http.server import BaseHTTPRequestHandler
import os
from pymongo import MongoClient
from bson import ObjectId
import json
from flask import Flask, Response
from api._util.validate import *
import * from passtoken as pt
app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['PUT', 'POST', 'GET', 'DELETE'])
@app.route('/<path:path>', methods=['PUT', 'POST', 'GET', 'DELETE'])
def catch_all(path):
    auth = pt.init_auth(os.environ['POSTGRES_URL'], os.environ['REDIS_URL'])
    if not pt.verify_token(auth, request.headers.get('token')):
        return Response("Unauthorized", mimetype='text/plain', status=401)
    from flask import request
    
    collection = "file_delete_paths"
    if request.headers.get("database"):
        collection += "_"
        collection += request.headers.get('database')
    
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
                client.data[collection].insert_one(validate_type(i, delete_type))
                response.append("OK")
            except:
                response.append("ERR")
        return Response(json.dumps(response), mimetype='application/json', status=200)
    
    elif request.method == 'GET':
        try:
            return Response(json.dumps([{key:str(value) if type(value) is ObjectId else value for key, value in item.items()} for item in list(client.data[collection].find(validate_query(body, delete_type)))]), mimetype='application/json')
        except:
            return Response(json.dumps({"Error": "bad shape"}), mimetype='application/json')
    
    elif request.method == 'POST':
        data = [(validate_query(i["query"], delete_type), i["update"]) for i in body]
        response = []
        for query, update in data:
            res = client.data[collection].update_many(query, update)
            response.append({"matched_count": res.matched_count, "modified_count": res.modified_count})
        return Response(json.dumps(response), mimetype='application/json')

    elif request.method == 'DELETE':
        data = client.data[collection].delete_many(validate_query(body, delete_type))
        return Response(json.dumps({"deleted": data.deleted_count}), mimetype='application/json')
