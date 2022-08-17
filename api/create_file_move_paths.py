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
        "curret": i["current"]
    } for i in body["data"]]
    MongoClient(os.environ['MONGODB_URI']).data.file_move_paths.insert_many([{j:i[j] for j in i.keys() if i[j] != None} for i in data])
    return Response("OK")
