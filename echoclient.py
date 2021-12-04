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
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = [60000,60001]       # The port used by the server
GLOBAL_STARTING = "AAAA"
GLOBAL_ENDING = "zzzz"
test_order = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capitalized = [x.capitalize() for x in test_order]
capitalized.extend(test_order)
cur_batch = []
cur_batch_pointer = 0
next_batch = []
batch_starting = GLOBAL_STARTING
batch_ending = shift(GLOBAL_STARTING,1000, capitalized)
on_off = [] #supports up to 5 workers maximum

#initial job batch setup
create_batch(GLOBAL_STARTING, cur_batch, capitalized, NUM_JOBS_IN_BATCH)

#connection setup
for i in range(NUM_WORKERS):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(10)
	s.connect((HOST, PORT[i]))
	#s.setblocking(0)
	WORKER_TRACKER[i] = s

print(WORKER_TRACKER)
input()
rs = WORKER_TRACKER[0]
rs2 = WORKER_TRACKER[1]
rs.sendall(bytes("0,AAAA,BBBB,cb08ca4a7bb5f9683c19133a84872ca7","utf-8"))
rs2.sendall(bytes("0,AAAA,BBBB,cb08ca4a7bb5f9683c19133a84872ca7","utf-8"))
dat = None
i = 0
#inf loop once initial jobs have been sent out
while(True):
	#check if number of workers changed

	ready = select.select([WORKER_TRACKER[i]], [], [], 0.1)
	if ready[0]:
		if i == 0:
			dat = rs.recv(4096)
			print("dat: ", dat)
			rs.sendall(bytes("0,AAAA,BBBB,cb08ca4a7bb5f9683c19133a84872ca7","utf-8"))
		elif i == 1:
			dat = rs2.recv(4096)
			print("dat: ", dat)
			rs2.sendall(bytes("0,AAAA,BBBB,cb08ca4a7bb5f9683c19133a84872ca7","utf-8"))
	i += 1
	if i > 1:
		i = 0

#inf loop, loop over