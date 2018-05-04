from flask import Flask, abort, jsonify
from werkzeug.exceptions import HTTPException, default_exceptions

app = Flask('test')


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code


for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)


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
