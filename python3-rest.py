#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import jsonify
from app import start
from flask_cors import CORS, cross_origin
import sys

app = Flask(__name__)
CORS(app)

token = sys.argv[1]

@app.route("/captura",methods=['POST'])
def entrenamiento_service():
    start(token)
    result = "Envio de imagen: OK"
    print(result)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8086)