# coding: utf-8
import json
from flask import Flask, request, redirect, url_for, jsonify
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/args")
def args():
    # http://localhost:8080/args?foo=bar
    return jsonify(request.args.to_dict())       # trans ImmutableMultiDict to dict


@app.route("/post", methods=['POST'])
def r_post():
    data = {}
    data['content-type'] = request.content_type
    data['form'] = request.form.to_dict()
    return jsonify(data)


@app.route("/redirect/with_args")
def redirect_with_args():
    return redirect(url_for('args', **request.args))
