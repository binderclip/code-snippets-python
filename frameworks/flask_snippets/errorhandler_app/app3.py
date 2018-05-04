from functools import wraps

from flask import Flask, abort, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code


def get_http_exception_handler(app):
    """Overrides the default http exception handler to return JSON."""
    handle_http_exception = app.handle_http_exception
    @wraps(handle_http_exception)
    def ret_val(exception):
        exc = handle_http_exception(exception)
        return jsonify(error=exc.description), exc.code
    return ret_val


# Override the HTTP exception handler.
app.handle_http_exception = get_http_exception_handler(app)


@app.route('/')
def index():
    return 'hello world'


@app.route("/500")
def error_500():
    a = 100 / 0
    return f'hello {a}'


@app.route("/r500")
def error_r500():
    abort(500)
    return 'hello'


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
