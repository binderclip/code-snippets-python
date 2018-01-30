# coding: utf-8
import json
from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/args")
def args():
    # http://localhost:8080/args?foo=bar
    return json.dumps(request.args)
