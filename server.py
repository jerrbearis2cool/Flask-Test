from flask import Flask, jsonify

app = Flask(__name__)

app.route("/hello_world", methods=["GET", "POST"])
def hello_world():
    return jsonify({"message": "hello world"})

if __name__ == "__main__":
	app.run(host="127.0.0.1", port=3333)
