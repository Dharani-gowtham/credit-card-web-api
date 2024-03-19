from flask import Flask
from pymongo import MongoClient


client = MongoClient()
db_name = client["credit_card"]

data = {
    "/": "homepage",
    "/cards":"Return all active cards -> Cards Object",
    "/update-gps": "Update the gps location from mobile for every 10 seconds -> None",
    "/purchase-request":"Validate the data from the mobile and laptop gps and store to logs-> Bool",
    "/add-card":"adding credit card to the db -> None",
    "/delete-card":"delting the credit card from db -> None",
    "/history":"returns transactions done"
}
app = Flask(__name__)

@app.route('/')
def homepage():
    return data



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=7896)