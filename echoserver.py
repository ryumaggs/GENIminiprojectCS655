import socket
import hashlib

from _thread import *
import threading

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65032        # Port to listen on (non-privileged ports are > 1023)
checked_ranges = {}
print_lock = threading.Lock()

def threaded(c):
    while True:
  
        # data received from client
        data = c.recv(1024)
        print(data)
        if not data:
            print('Bye')
              
            # lock released on exit
            print_lock.release()
            break
  
        # reverse the given string from client
        data = data[::-1]
  
        # send back reversed string to client
        c.send(data)
  
    # connection closed
    c.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)
while True:
    conn, addr = s.accept()
    print_lock.acquire()
    print('Connected to :', addr[0], ':', addr[1])

    # Start a new thread and return its identifier
    w = threading.Thread(target=threaded, args=(conn,))
    w.start()
    w.join()
    break