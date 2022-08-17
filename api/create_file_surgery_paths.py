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
    try: body = request.form if type(request.json) is dict else {}
    except: body = {}
    data = [{
        "name": i["name"] if "name" in i.keys() else None,
        "new": i["new"],
        "curret": i["current"],
        "redirect": i["redirect"] if "redirect" in i.keys() else None
    } for i in body["data"]]
    return Response(json.dumps([{j:i[j] for j in i.keys() if i[j] != None} for i in data]), mimetype='application/json')
