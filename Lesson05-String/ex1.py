'''
string pretty print 

'''

RANGE1 = [1, 9]
RANGE2 = [1, 9]

def calc(a,b):
    return [
        {'sign': '*', 'result':a*b},
    ]

for i in range(RANGE1[0],RANGE1[1] + 1):
    for j in range(RANGE2[0], RANGE2[1] + 1):
        for k in calc(i, j):
            print(str(i) + str(k['sign']) + str(j) + '=' + '{0:>2}'.format(str(k['result'])), end=" | ")
    print()
