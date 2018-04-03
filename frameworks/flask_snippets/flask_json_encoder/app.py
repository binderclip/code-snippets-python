import datetime
from flask import Flask, jsonify
from flask.json import JSONEncoder


class MyJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, datetime.datetime):
                return obj.strftime('%Y-%m-%d %H:%M:%S')
            iterable = iter(obj)
        except TypeError as e:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


app = Flask(__name__)
app.json_encoder = MyJSONEncoder


@app.route("/")
def hello():
    now = datetime.datetime.now()
    return jsonify({"now": now, 'foo': range(10)})


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()

# http://flask.pocoo.org/snippets/119/
