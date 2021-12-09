from flask import Flask, request, abort
import time

app = Flask(__name__)

from echoclient import solve
from echoclienttext import to_text

@app.route('/decrypt', methods=["POST"], strict_slashes=False)
def decryptPassword():
    hashs = request.json['hash']
    num = request.json['num']
    # print(hashs)
    # print(num)
    ret = solve(hashs, num)
    # print("ret: ", ret)
    # return {'time': time.time()}
    return {'dpass': ret}

@app.route('/change', methods=['POST'])
def changeNumberNodes():
    num = request.json['num']
    to_text(num) 
    return {'hi': True}