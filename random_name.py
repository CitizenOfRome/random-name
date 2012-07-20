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
if arglen>4:
    user = str(sys.argv[4]).lower()
    if user[0]=="-":
        '''Avoid letters'''
        filter_func = lambda x: x not in user
    else:
        '''Use letters'''
        filter_func = lambda x: x in user
    vowels = filter(filter_func, vowels)
    if len(vowels)==0: vowels = ['']
    consonants = filter(filter_func, consonants)
    if len(consonants)==0: consonants = ['']

print ""
print "Limit:", limit
print "Max-Length:", end-1
print "Min-Length:", start
print "Vowels used:", "".join(vowels)
print "Consonants used:", "".join(consonants)

def random_select(vow, con, count):
    '''Generate a  pronounceable name from the given vowels and consonants'''
    ret = []
    i = 0
    while i < count:
        ran = []
        if i > 0:
            '''Prevent two vowels or consonants from being together'''
            if ret[-1][-1] in vowels:
                ran = [random.choice(con), random.choice(vow)]
            else:
                ran = [random.choice(vow), random.choice(con)]
        else: 
            ran = [random.choice(vow), random.choice(con)]
            random.shuffle(ran)
        ran = "".join(ran)
        i+= len(ran)
        ret.append(ran)
    return "".join(ret)[:count]
	
def random_select_n(vow, con, count, limit):
    '''Iterate over random_select till limit is reached'''
    ret = []
    for i in xrange(limit):
        tmp = (random_select(vow, con, count))
        l=0
        while tmp in ret:
            tmp = (random_select(vow, con, count))
            l+=1
            if l>500: break
        ret.append(tmp)
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


