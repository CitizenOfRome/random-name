import sys
import random

okay = ['ab', 'ac', 'ad', 'af', 'ag', 'ah', 'aj', 'ak', 'al', 'am', 'an', 'ap', 'aq', 'ar', 'as', 'at', 'av', 'aw', 'ax', 'az', 'be', 'bi', 'bo', 'bu', 'by', 'ce', 'ci', 'co', 'cu', 'cy', 'de', 'di', 'do', 'du', 'dy', 'ef', 'eg', 'eh', 'ej', 'ek', 'el', 'em', 'en', 'ep', 'eq', 'er', 'es', 'et', 'ev', 'ew', 'ex', 'ez', 'fi', 'fo', 'fu', 'fy', 'gi', 'go', 'gu', 'gy', 'hi', 'ho', 'hu', 'hy', 'ij', 'ik', 'il', 'im', 'in', 'ip', 'iq', 'ir', 'is', 'it', 'iv', 'iw', 'ix', 'iz', 'jo', 'ju', 'jy', 'ko', 'ku', 'ky', 'lo', 'lu', 'ly', 'mo', 'mu', 'my', 'no', 'nu', 'ny', 'op', 'oq', 'or', 'os', 'ot', 'ov', 'ow', 'ox', 'oz', 'pl', 'pu', 'py', 'qu', 'qy', 'ru', 'ry', 'sc', 'sch', 'scr', 'sh', 'shr', 'sk', 'sl', 'sm', 'sn', 'sp', 'sph', 'spl', 'spr', 'squ', 'str', 'su', 'sy', 'th', 'thr', 'tr', 'tu', 'ty', 'uv', 'uw', 'ux', 'uz', 'vy', 'wh', 'wr', 'wy', 'xy', 'yz']
random.shuffle(okay)

arglen = len(sys.argv)
start = 2
end = 3
limit = 10
if arglen>1: limit = int(sys.argv[1])
if arglen>2: end = int(sys.argv[2])+1
if arglen>3: start = int(sys.argv[3])
else: start = end-1

def ranom_select(arr, count):
	if len(arr)==0: return []
	ret = []
	for i in xrange(count):
		ret.append(random.choice(arr))
	return ret
	
def random_select_n(arr, count, limit):
	ret = []
	for i in xrange(limit):
		ret.append(ranom_select(arr, count))
	return ret

print ""
for i in xrange(start, end):
	combos = random_select_n(okay, i, limit)
	j = 0
	for item in combos:
		print "".join(item)
		j += 1
		if j > limit: break
	print ""


