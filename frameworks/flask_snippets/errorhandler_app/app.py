from flask import Flask
app = Flask(__name__)


@app.errorhandler(404)
def app_404(e):
    print(e)
    print(type(e))
    return 'page not found', 404


@app.route("/")
def hello():
    return "Hello World!"


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
