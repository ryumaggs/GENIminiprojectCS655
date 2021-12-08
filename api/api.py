import time
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/time', methods=["POST"], strict_slashes=False)
def get_current_time():
    hash = request.json['hash']
    num = request.json['num']
    print(hash)
    print(num)
    print("Hello World")
    return {'time': time.time()}