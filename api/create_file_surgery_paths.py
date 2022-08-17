from http.server import BaseHTTPRequestHandler
import os
from pymongo import MongoClient
import json
from flask import Flask, Response
app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['PUTS'])
@app.route('/<path:path>', methods=['PUTS'])
def catch_all(path):
    from flask import request
    if request.headers.get('Content-Type') != 'application/json': return Response("Content-Type must be application/json", mimetype='text/plain', status=400)
    body = request.json
    data = [{
        "name": i["name"] if "name" in i.keys() else None,
        "new": i["new"],
        "curret": i["current"],
        "redirect": i["redirect"] if "redirect" in i.keys() else None
    } for i in body["data"]]
    client = MongoClient(os.environ['MONGODB_URI'])
    client.data.file_surgery_paths.insert_many(data)
    return Response("OK", mimetype='text/plain', status=200)
