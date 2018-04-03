from flask import Blueprint, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__)

@simple_page.route('/', defaults={'name': 'foo'})
@simple_page.route('/<name>')
def show(name):
    try:
        return name
    except TemplateNotFound:
        abort(404)
