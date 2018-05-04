from flask import Flask, abort
app = Flask(__name__)


@app.errorhandler(404)
def app_404(e):
    print(e)
    print(type(e))
    return 'page not found', 404


@app.errorhandler(500)
def app_500(e):
    print(e)
    print(type(e))
    return 'page error', 500


@app.errorhandler(ZeroDivisionError)
def app_500(e):
    print(e)
    print(type(e))
    return 'ZeroDivisionError', 500


@app.errorhandler(ZeroDivisionError)
def app_500(e):
    print(e)
    print(type(e))
    return 'ZeroDivisionError', 500



@app.route("/")
def hello():
    return "Hello World!"


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
