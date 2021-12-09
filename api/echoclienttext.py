# from __main__ import app

# @app.route('/change', methods=['POST'])
def to_text(num):
	# num = request.json['num']
	o_file = open("num_worker.txt",'w')
	print(str(num),file=o_file,end='')
	o_file.close()
	