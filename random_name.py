import sys
import random

vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

arglen = len(sys.argv)
start = 2
end = 3
limit = 10
if arglen>1: limit = int(sys.argv[1])
if arglen>2: end = int(sys.argv[2])+1
if arglen>3: start = int(sys.argv[3])
else: start = end-1

def ranom_select(vow, con, count):
	ret = []
	for i in xrange(count):
		ran = [random.choice(vow),random.choice(con)]
		random.shuffle(ran)
		ret.append("".join(ran))
	return ret
	
def random_select_n(vow, con, count, limit):
	ret = []
	for i in xrange(limit):
		ret.append(ranom_select(vow, con, count))
	return ret

print ""
for i in xrange(start, end):
	combos = random_select_n(vowels, consonants, i, limit)
	j = 0
	for item in combos:
		print "".join(item)
		j += 1
		if j > limit: break
	print ""


