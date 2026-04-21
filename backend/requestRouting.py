from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_test', methods=['GET'])
def get_test():
    return jsonify("Got me from python script")

@app.route('/post_test', methods=['POST'])
def post_test():
    data = request.json
    print("python got: ", data)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)