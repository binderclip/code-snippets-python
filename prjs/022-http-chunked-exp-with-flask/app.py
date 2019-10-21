import time
from flask import Flask, escape, request, Response

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/stream.csv')
def generate_large_csv():
    def generate():
        print("== generate start ==")
        for i in range(10000):
            yield f'{i}, foo\n'
            time.sleep(0.0005)
        print("== generate done ==")
    return Response(generate(), mimetype='text/csv')


def main():
    app.run(port=8889)


if __name__ == '__main__':
    main()
