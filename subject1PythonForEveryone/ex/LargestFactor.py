import math

def Prime(num):
	l = list(range(2,num+1))
	for i in range(2,int(math.sqrt(num)+1)):
		for j in range (i*i, num+1, i):
			if j in l:
				l.remove(j)
	return l	

t = int(input())
res = Prime(1000)

for i in range(t):
    n = int(input())
    i = 2
    d = 0
    maxx = 0
    for i in res:
        if n % i == 0:
            while (n != 1) and (n % i == 0):
                n //= i
            if maxx < i: maxx = i
    if maxx == 0: maxx = n
    print(maxx)

#1/20