from flask import Flask, jsonify, request
from pymongo import MongoClient
from database import add_credit_card, get_credit_cards
from bson import json_util

client = MongoClient()
db_name = client["credit_card"]

data = {
    "/": "homepage",
    "/add-card":"adding credit card to the db -> None",
    "/delete-card":"delting the credit card from db -> None",
    "/cards":"Return all active cards -> Cards Object",
    "/update-gps": "Update the gps location from mobile for every 10 seconds -> None",
    "/purchase-request":"Validate the data from the mobile and laptop gps and store to logs-> Bool",
    "/history":"returns transactions done"
}
app = Flask(__name__)

@app.route('/')
def homepage():
    return data

@app.route('/add-card', methods=['POST'])
def add_card():
    data = request.get_json()
    print(data)
    # add_credit_card()
    return "add_card"

@app.route('/delete-card', methods=['DELETE'])
def delete_card():
    return "delete card"

@app.route('/cards', methods=['GET'])
def cards():
    data = json_util.dumps(get_credit_cards())
    return jsonify(data)

@app.route('/update-gps', methods=['POST'])
def update_gps():
    return "Update GPS"

@app.route('/purchase-request', methods=['POST'])
def purchase_request():
    return "Purchase Request"

@app.route("/history", methods=['GET'])
def history():
    return "history"



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=7896)