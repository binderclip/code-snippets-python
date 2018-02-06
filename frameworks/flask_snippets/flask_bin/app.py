# coding: utf-8
import json
from flask import Flask, request, redirect, url_for
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/args")
def args():
    # http://localhost:8080/args?foo=bar
    return json.dumps(request.args)


@app.route("/redirect/with_args")
def redirect_with_args():
    return redirect(url_for('args', **request.args))
