# coding: utf-8
from my_app.app import app
from flask_mako import render_template


@app.route("/")
def index():
    return render_template('index.html', name='Big WM')
