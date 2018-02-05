# coding: utf-8
from flask import Flask
from flask_mako import MakoTemplates
app = Flask(__name__)
mako = MakoTemplates(app)

import my_app.views.hello
