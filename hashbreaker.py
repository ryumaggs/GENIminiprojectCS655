import hashlib

starting_str = "AAAAA"
ending_str = "AAzzz"

correct_str = "BBBBB"
#correct_hash = 	"31c42d123b6bfdb748bfbaef78e1ea70"
correct_hash = ""
 
test_order = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capitalized = [x.capitalize() for x in test_order]

capitalized.extend(test_order)


def increment(cur_str):
	indexes = []
	for i in range(len(cur_str)):
		indexes.append(capitalized.index(cur_str[i]))

	overflow = 0
	for i in reversed(range(len(indexes))):
		indexes[i] += 1
		overflow = 0

		if indexes[i] >= len(capitalized):
			overflow = 1
			indexes[i] = 0

		if overflow == 0:
			break

	ret_str = ""
	for i in range(len(indexes)):
		ret_str += capitalized[indexes[i]]

	print(ret_str)
	return ret_str

def checkrange(starting, ending):
	cur_str = starting
	while(True):
		result = hashlib.md5(cur_str.encode())
		check = (result.hexdigest() == (correct_hash))
		if check:
			return True, cur_str
		cur_str = increment(cur_str)
		if cur_str == ending:
			break
	return False, None

in_range, sol = checkrange(starting_str, ending_str)

print("in range?: ", in_range, "answer is: ", sol)