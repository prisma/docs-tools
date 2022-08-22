from http.server import BaseHTTPRequestHandler
import os
from pymongo import MongoClient
import json
from flask import Flask, Response
app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['PUT', 'POST', 'GET', 'DELETE'])
@app.route('/<path:path>', methods=['PUT', 'POST', 'GET', 'DELETE'])
def catch_all(path):
    from flask import request
    
    client = MongoClient(os.environ['MONGODB_URI'])
    
    if request.method == 'PUT':
        if request.headers.get('Content-Type') != 'application/json': return Response("Content-Type must be application/json", mimetype='text/plain', status=400)
        body = request.json
        response = []
        def format(i):
            try:
                formated = {
                    "name": i["name"] if "name" in i.keys() else None,
                    "new": i["new"],
                    "current": i["current"]
                }
                response.append("OK")
                return formated
            except:
                response.append("ERR")
                return None
        data = [j for j in [format(i) for i in body["data"]] if j != None]
        client.data.file_move_paths.insert_many([{j:i[j] for j in i.keys() if i[j] != None} for i in data])
        client.data.changes.insert_one({})
        return Response(json.dumps(response), mimetype='application/json', status=200)
    
    elif request.method == 'GET':
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
        data = [{
            "_id": str(i["_id"]),
            "name": i["name"] if "name" in i.keys() else None,
            "current": i["current"],
            "new": i["new"]
            } for i in client.data.file_move_paths.find(args)]
        client.data.changes.insert_one({})
        return Response(json.dumps([{j:i[j] for j in i.keys() if i[j] != None} for i in data]), mimetype='application/json')

    elif request.method == 'POST':
        if request.headers.get('Content-Type') != 'application/json': return Response("Content-Type must be application/json", mimetype='text/plain', status=400)
        body = request.json

        data = [(i["query"], i["update"]) for i in body]
        return response(json.dumps(data), mimetype='application/json')

    
    elif request.method == 'DELETE':
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
        data = client.data.file_move_paths.delete_many(args)
        client.data.changes.insert_one({})
        return Response(json.dumps({"deleted": data.deleted_count}), mimetype='application/json')
