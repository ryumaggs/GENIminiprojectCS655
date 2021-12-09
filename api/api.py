from flask import Flask, request, abort
import time

app = Flask(__name__)

from echoclient import solve
from echoclienttext import to_text

@app.route('/time', methods=["POST"], strict_slashes=False)
def get_current_time():
    hash = request.json['hash']
    num = request.json['num']
    print(hash)
    print(num)
    solve(hash, num)
    # print("Hello World")
    # return {'time': time.time()}

@app.route('/change', methods=['POST'])
def get_current_time2():
    num = request.json['num']
    to_text(num) 