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

#global variables
NUM_WORKERS = 2
NUM_JOBS_IN_BATCH = 1000
WORKER_TRACKER = {}
HOST = ['127.0.0.1','127.0.0.1']  # The server's hostname or IP address
PORT = [60000,60001]       # The port used by the server
GLOBAL_STARTING = "AAAA"
GLOBAL_ENDING = "zzzz"

#begin loop here: 
while True:
	print("enter code to break: ")
	GLOBAL_SOLUTION = input() #get this from webpage
	test_order = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	capitalized = [x.capitalize() for x in test_order]
	capitalized.extend(test_order)
	cur_batch = []
	cur_batch_status = []
	cur_batch_pointer = 0
	next_batch = []
	batch_starting = GLOBAL_STARTING
	batch_ending = shift(GLOBAL_STARTING,1000, capitalized)
	on_off = [] #supports up to 5 workers maximum

	#initial job batch setup. create_batch, and the reset of cur_batch_pointer should always be called together
	cur_str = create_batch(GLOBAL_STARTING, cur_batch, cur_batch_status, capitalized, NUM_JOBS_IN_BATCH)
	cur_batch_pointer = 0

	#connection setup
	for i in range(NUM_WORKERS):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(10)
		s.connect((HOST[i], PORT[i]))
		#s.setblocking(0)
		WORKER_TRACKER[i] = s

	print(WORKER_TRACKER)
	input()
	#send initial jobs
	for i in range(NUM_WORKERS):
		job_str = "0,"+cur_batch[cur_batch_pointer][0]+","+cur_batch[cur_batch_pointer][1]+","+GLOBAL_SOLUTION
		WORKER_TRACKER[i].sendall(bytes(job_str,"utf-8"))
		cur_batch_pointer += 1


	dat = None
	i = 0
	#inf loop once initial jobs have been sent out
	while(True):
		#check if number of workers changed
		ready = select.select([WORKER_TRACKER[i]], [], [], 0.01)
		if ready[0]:
			dat = WORKER_TRACKER[i].recv(4096)
			data_str = dat.decode("utf-8")
			splitt = data_str.split(',')
			if splitt[0] == "T":
				print("Answer found: ", splitt[1])
				break
			job_str = "0,"+cur_batch[cur_batch_pointer][0]+","+cur_batch[cur_batch_pointer][1]+","+GLOBAL_SOLUTION
			WORKER_TRACKER[i].sendall(bytes(job_str,"utf-8"))
			cur_batch_pointer += 1

			if cur_batch_pointer >= len(cur_batch):
				cur_batch = []
				cur_batch_status = []
				cur_str = create_batch(cur_str, cur_batch, cur_batch_status, capitalized, NUM_JOBS_IN_BATCH)
				cur_batch_pointer = 0

		i += 1
		if i > (NUM_WORKERS-1):
			i = 0

	#close connections once answer is found
	for i in range(NUM_WORKERS):
		WORKER_TRACKER[i].sendall(bytes("tt","utf-8"))
	#inf loop, loop over