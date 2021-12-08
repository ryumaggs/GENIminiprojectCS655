#!/usr/bin/env python3
'''
Will have to use multiprocessing instead of threading. honestly what is even the point of the python threading module

Actually. I don't even need to do any threading or multiprocessing.

Just have one function that connects to all workers and stores it in a variable
'''
import socket
import time
from util import create_batch, checkrange, increment, shift
import select

def solve():
	#variables that need to be set: int
	NUM_WORKERS = 0

	#str: the md5 hash that needs to be solved
	GLOBAL_SOLUTION = None 

	#global variables
	worker_txt_path = "./num_worker.txt"
	MAX_WORKERS = 4
	NUM_JOBS_IN_BATCH = 1000
	WORKER_TRACKER = {}
	WEBSERVER_HOST = '127.0.0.1'
	WEBSERVER_PORT = 59999
	HOST = ['127.0.0.1','127.0.0.1', '127.0.0.1', '127.0.0.1']  # The server's hostname or IP address
	PORT = [60000,60001, 60002, 60003]       # The port used by the server
	GLOBAL_STARTING = "AAAAA"
	GLOBAL_ENDING = "ZZZZZ"

	test_order = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	capitalized = [x.capitalize() for x in test_order]
	capitalized.extend(test_order)

	#self.WEBSERVER_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#self.WEBSERVER_s.connect((WEBSERVER_HOST, WEBSERVER_PORT))


	#begin loop here: 
	'''
	while True:
		dat = WEBSERVER_s.recv(1024).decode("utf-8")
		dat_split = dat.split(",")
		print(dat_split)
		if len(dat_split) == 3:
			NUM_WORKERS = int(dat_split[1])
			GLOBAL_SOLUTION = dat_split[2]
			break
	WEBSERVER_s.sendall(bytes("setup complete","utf-8"))
	'''

	cur_batch = []
	cur_batch_status = []
	cur_batch_pointer = 0
	next_batch = []
	batch_starting = GLOBAL_STARTING
	batch_ending = shift(GLOBAL_STARTING,1000, capitalized)
	on_off = [] #supports up to 5 workers maximum
	for i in range(NUM_WORKERS):
		on_off.append(1)
	for i in range(MAX_WORKERS-NUM_WORKERS):
		on_off.append(0)

	#initial job batch setup. create_batch, and the reset of cur_batch_pointer should always be called together
	cur_str = create_batch(GLOBAL_STARTING, cur_batch, cur_batch_status, capitalized, NUM_JOBS_IN_BATCH)
	cur_batch_pointer = 0

	#connection setup
	for i in range(MAX_WORKERS):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(10)
		s.connect((HOST[i], PORT[i]))
		#s.setblocking(0)
		WORKER_TRACKER[i] = s

	#send initial jobs
	for i in range(MAX_WORKERS):
		if on_off[i] == 1:
			job_str = "0,"+cur_batch[cur_batch_pointer][0]+","+cur_batch[cur_batch_pointer][1]+","+GLOBAL_SOLUTION
			WORKER_TRACKER[i].sendall(bytes(job_str,"utf-8"))
			cur_batch_pointer += 1
			for i in range(NUM_WORKERS):
				on_off.append(1)
			for i in range(MAX_WORKERS-NUM_WORKERS):
				on_off.append(0)

	dat = None
	i = 0
	#inf loop once initial jobs have been sent out
	##loop through workers
	while(True):
		#check if number of workers changed

		#check textfile here
		i_file = open("./num_worker.txt",'r')
		line = i_file.readline()
		NUM_WORKERS = int(line)
		i_file.close()


		ready = select.select([WEBSERVER_s], [], [], 0.000001)
		if ready[0]:
			dat = WEBSERVER_s.recv(1028)
			data_str = dat.decode("utf-8")
			if data_str != "":
				print("d: ", data_str)
				data_split = data_str.split(",")
				new_num_workers = int(data_split[1])
				NUM_WORKERS = new_num_workers
				on_off = []
				for i in range(NUM_WORKERS):
					on_off.append(1)
				for i in range(MAX_WORKERS-NUM_WORKERS):
					on_off.append(0)
				print("new num worker: ", on_off)
				WEBSERVER_s.sendall(bytes("workers changed","utf-8"))

		ready = select.select([WORKER_TRACKER[i]], [], [], 0.01)
		if ready[0]:
			dat = WORKER_TRACKER[i].recv(4096)
			data_str = dat.decode("utf-8")
			splitt = data_str.split(',')
			if splitt[0] == "T":
				print("Answer found: ", splitt[1])
				WEBSERVER_s.sendall(bytes("Answer found,"+splitt[1],"utf-8"))
				break

		if on_off[i] == 1:
			job_str = "0,"+cur_batch[cur_batch_pointer][0]+","+cur_batch[cur_batch_pointer][1]+","+GLOBAL_SOLUTION
			WORKER_TRACKER[i].sendall(bytes(job_str,"utf-8"))
			cur_batch_pointer += 1

			if cur_batch_pointer >= len(cur_batch):
				cur_batch = []
				cur_batch_status = []
				cur_str = create_batch(cur_str, cur_batch, cur_batch_status, capitalized, NUM_JOBS_IN_BATCH)
				cur_batch_pointer = 0

		i += 1
		if i > (MAX_WORKERS-1):
			i = 0

	#close connections once answer is found
	for i in range(NUM_WORKERS):
		WORKER_TRACKER[i].sendall(bytes("tt","utf-8"))
	#inf loop, loop over