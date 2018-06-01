from flask import Flask

from frameworks.flask_snippets.before_after_request_sp.bp import bp

app = Flask(__name__)
app.register_blueprint(bp, url_prefix='/bp')


@app.before_request
def before_request():
    print('>>> before_request')


@app.after_request
def after_request(resp):
    print('>>> after_request')
    print(resp)
    return resp


@app.route("/", methods=['GET', 'POST'])
def index():
    return "Hello World!"


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
