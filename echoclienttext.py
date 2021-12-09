from echoclient import solve
def to_text():
	o_file = open("num_worker.txt",'w')
	print(str(3),file=o_file,end='')
	o_file.close()