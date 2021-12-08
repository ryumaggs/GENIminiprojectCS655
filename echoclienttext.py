def to_text(num_workers):
	o_file = open("numw.txt",'w')
	print(str(num_workers),file=o_file)
	o_file.close()