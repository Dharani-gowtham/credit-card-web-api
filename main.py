from flask import Flask
import time

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
    time.sleep(5)
    data = {'data': 'Hello'}
    return data


if __name__ == '__main__':
    app.run(debug=True)