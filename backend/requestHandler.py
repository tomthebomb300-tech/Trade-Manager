from flask import Flask, request, jsonify
from flask_cors import CORS
from data import *

app = Flask(__name__)
CORS(app)

df = startup()

@app.route('/get_profit_loss', methods=['GET'])
def get_profit_loss():
    return jsonify(getProfitLoss(df))


@app.route('/get_win_rate', methods=['GET'])
def get_win_rate():
    return jsonify(getWinRate(df))


@app.route('/get_average_win', methods=['GET'])
def get_average_win():
    return jsonify(getAvgProfit(df))


@app.route('/get_average_loss', methods=['GET'])
def get_average_loss():
    return jsonify(getAvgLoss(df))


@app.route('/get_profit_factor', methods=['GET'])
def get_profit_factor():
    return jsonify(getProfitFactor(df))

@app.route('/get_daily_PL', methods=['GET'])
def get_daily_PL():
    return jsonify(getDailyPL(df))


@app.route('/post_test', methods=['POST'])
def post_test():
    data = request.json
    print("python got: ", data)
    return jsonify({"status": "success"})


if __name__ == '__main__':
    app.run(debug=True)