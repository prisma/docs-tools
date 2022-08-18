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
    if request.headers.get('Content-Type') != 'application/json': return Response("Content-Type must be application/json", mimetype='text/plain', status=400)
    body = request.json
    client = MongoClient(os.environ['MONGODB_URI'])
    changes = sum([i for i in client.data.changes.find()])
    if "delete" in body.keys():
        if body["delete"]:
            client.data.changes.delete_many({})
    return Response(json.dumps({"count": changes}), mimetype='application/json')