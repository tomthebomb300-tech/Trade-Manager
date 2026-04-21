from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/add_trade', methods=['POST'])
def add_trade():
    data = request.json
    print(data)
    return jsonify({"status": "success"})

@app.route('/get_trades', methods=['GET'])
def get_trades():
    trades = [
        {"symbol": "AAPL", "profit": 120},
        {"symbol": "TSLA", "profit": -50}
    ]
    return jsonify(trades)

if __name__ == '__main__':
    app.run(debug=True)