from flask import Flask, request, jsonify
app = Flask(__name__)



@app.route("/")
def get():
    return "Hello World!"



@app.route("/get", methods=['GET'])
def app_get():
    print(request.headers)
    return jsonify({
        "args": request.args,
    })


@app.route("/post", methods=['POST'])
def app_post():
    return jsonify({
        "json": request.json,
        "form": request.form,
    })


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
