import socket
import hashlib
from util import checkrange, increment
import sys
import random
import time

def parse_msg(msg):
    #msg is a string
    split = msg.split(',')
    typee = int(split[0])
    start = split[1]
    end = split[2]
    correct = split[3]
    return typee, start, end, correct

#network setup

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = int(sys.argv[1])        # Port to listen on (non-privileged ports are > 1023)
checked_ranges = {}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

while True:
    print("Waiting for connection....")
    s.settimeout(10)
    s.listen(1)
    conn, addr = s.accept()
    print('Connected to :', addr[0], ':', addr[1])

    #hash breaking setup
    #data = "0,AAAA,BBBB,cb08ca4a7bb5f9683c19133a84872ca7"
    test_order = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    capitalized = [x.capitalize() for x in test_order]

    capitalized.extend(test_order)

    old_results = []

    pointer = 0

    while True:
        #sleept = random.random()
        #print("sleeping for: ", sleept)
        #time.sleep(sleept)
        data = conn.recv(1024)
        data_str = data.decode("utf-8")
        print("dr: ", data_str)
        if data_str == "tt":
            conn.close()
            break
        typee, starting_str, ending_str, correct_str = parse_msg(data_str)
        if typee == 0:
            res,stringg = checkrange(starting_str,ending_str, correct_str, capitalized)
            if res:
                conn.sendall(bytes("T,"+stringg,"utf-8"))
            else:
                conn.sendall(bytes("F,"+stringg,"utf-8"))

            if len(old_results) < 1000:
                old_results.append((starting_str,ending_str,res))
            else:
                old_results[pointer] = ((starting_str,ending_str,res))
            pointer += 1
            if pointer >= 1000:
                pointer = 0
