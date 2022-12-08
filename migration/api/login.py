import * from passtoken as pt
from flask import Flask, Response


@app.route('/', defaults={'path': ''}, methods=['PUT', 'POST', 'GET', 'DELETE'])
@app.route('/<path:path>', methods=['PUT', 'POST', 'GET', 'DELETE'])
def catch_all(path):
    auth = pt.init_auth(os.environ['POSTGRES_URL'], os.environ['REDIS_URL'])
    from flask import request
    try:
        return Response("{token:" + auth.login(request.headers.get('email'), request.headers.get('password')) + "}", mimetype='application/json', status=200)
    except Exception as e:
        return Response("{{error:Unauthorized}}", mimetype='application/json', status=401)