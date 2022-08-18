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
        response = []
        def format(i):
            try:
                formated = {
                    "name": i["name"] if "name" in i.keys() else None,
                    "path": i["path"],
                    "redirect": i["redirect"] if "redirect" in i.keys() else None
                }
                response.append("OK")
                return formated
            except:
                response.append("ERR")
                return None
        data = [j for j in [format(i) for i in body["data"]] if j != None]
        MongoClient(os.environ['MONGODB_URI']).data.file_delete_paths.insert_many([{j:i[j] for j in i.keys() if i[j] != None} for i in data])
        return Response({"checks":response}, mimetype='application/json', status=200)
    
    elif request.method == 'GET':
        if request.headers.get('Content-Type') != 'application/json': return Response("Content-Type must be application/json", mimetype='text/plain', status=400)
        body = request.json
        args = {}
        if "_id" in body.keys():
            args["_id"] = body["_id"]
        if "name" in body.keys():
            args["name"] = body["name"]
        if "path" in body.keys():
            args["path"] = body["path"]
        if "redirect" in body.keys():
            args["redirect"] = body["redirect"]
        client = MongoClient(os.environ['MONGODB_URI'])
        data = [{
            "_id": str(i["_id"]),
            "name": i["name"] if "name" in i.keys() else None,
            "path": i["path"],
            "redirect": i["redirect"] if "redirect" in i.keys() else None
            } for i in client.data.file_delete_paths.find(args)]
        return Response(json.dumps([{j:i[j] for j in i.keys() if i[j] != None} for i in data]), mimetype='application/json')
    
    elif request.method == 'DELETE':
        if request.headers.get('Content-Type') != 'application/json': return Response("Content-Type must be application/json", mimetype='text/plain', status=400)
        body = request.json
        args = {}
        if "_id" in body.keys():
            args["_id"] = body["_id"]
        if "name" in body.keys():
            args["name"] = body["name"]
        if "path" in body.keys():
            args["path"] = body["path"]
        if "redirect" in body.keys():
            args["redirect"] = body["redirect"]
        client = MongoClient(os.environ['MONGODB_URI'])
        data = client.data.file_delete_paths.delete_many(args)
        
        return Response(json.dumps({"deleted": data.deleted_count}), mimetype='application/json')
