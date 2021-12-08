def to_text():
	o_file = open("numw.txt",'w')
	print(str(num_workers),file=o_file)
	o_file.close()