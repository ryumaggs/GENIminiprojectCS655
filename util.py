'''
This file contains functions that can be shared by server and client

All of them involve some process of iterating over a 5 string value

Where each char in the string can be between A - z (lower case)

'''
import hashlib
def create_batch(start_str, arr, capitalized, NUM_JOBS_IN_BATCH):
	cur_str = start_str
	for i in range(NUM_JOBS_IN_BATCH):
		end_str = shift(cur_str, 300, capitalized)
		arr.append((cur_str, end_str))
		cur_str = end_str
	return cur_str

def checkrange(starting, ending, correct_hash, capitalized):
    cur_str = starting
    while(True):
        result = hashlib.md5(cur_str.encode())
        check = (result.hexdigest() == (correct_hash))
        if check:
            return True, cur_str
        cur_str = increment(cur_str, capitalized)
        if cur_str == ending:
            break
    return False, None


def increment(cur_str, capitalized):
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
    return ret_str

def shift(starting, num, capitalized):
	cur = starting
	for i in range(num):
		cur = increment(cur, capitalized)
	return cur
