from http.server import BaseHTTPRequestHandler
import os
from pymongo import MongoClient
import json
from flask import Flask, Response
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    from flask import request
    try: body = request.form if type(request.form) is dict else {}
    except: body = {}
    args = {}
    if "_id" in body.keys():
        args["_id"] = body["_id"]
    if "name" in body.keys():
        args["name"] = body["name"]
    if "current" in body.keys():
        args["current"] = body["current"]
    if "new" in body.keys():
        args["new"] = body["new"]
    client = MongoClient(os.environ['MONGODB_URI'])
    data = [{
        "_id": str(i["_id"]),
        "name": i["name"] if "name" in i.keys() else None,
        "current": i["current"],
        "new": i["new"]
        } for i in client.data.file_move_paths.find(args)]
    return Response(body)
    return Response(json.dumps([{j:i[j] for j in i.keys() if i[j] != None} for i in data]), mimetype='application/json')
