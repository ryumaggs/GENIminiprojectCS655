import socket
import random
import time
import select

WEBSERVER_HOST = '127.0.0.1'
WEBSERVER_PORT = 59999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((WEBSERVER_HOST, WEBSERVER_PORT))
s.settimeout(30) #added this bc on windows the timeout is indefinite and blocking
s.listen(1)
conn, addr = s.accept()

while(True):
	print("enter the number of workers: ")
	NUM_WORKERS = input()
	print("enter the hashcode to be deciphered: ")
	MD5_HASH = input()
	conn.sendall(bytes("0,"+str(NUM_WORKERS)+","+MD5_HASH,"utf-8"))
	data = conn.recv(1024).decode("utf-8")
	print(data)
	time.sleep(3)
	#wait for response from the master that the number of workers has been correctly received

	while True:
		ready = select.select([s], [], [], 0.000001)
		if ready[0]:
			data = conn.recv(1024).decode("utf-8")
			if "Answer" in data:
				print('found answer')
				break
		time.sleep(5)
		NUM_WORKERS_NEW = random.randint(1,4)
		if NUM_WORKERS != NUM_WORKERS_NEW:
			conn.sendall(bytes("2,"+str(NUM_WORKERS_NEW),"utf-8"))
			NUM_WORKERS = NUM_WORKERS_NEW
			data = conn.recv(1024).decode("utf-8")
			print(data)
			if "Answer" in data:
				print('found answer')
				break
