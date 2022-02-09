import math

def Prime(num):
	l = list(range(2,num+1))
	for i in range(2,int(math.sqrt(num)+1)):
		for j in range (i*i, num+1, i):
			if j in l:
				l.remove(j)
	return l

def tcs(num):
    s = 0
    while num != 0:
        s += num % 10
        num //= 10 
    return s

t = int(input())
res = Prime(10000)

for i in range(t):
    n = int(input())
    n2 = n
    sum = 0
    for i in res:
        if i != n2:
            if n % i == 0:
                d = 0
                while (n != 1) and (n % i == 0):
                    n //= i
                    d += 1
                sum += tcs(i) * d
    
    if tcs(n2) == sum:
        print(1)
    else:
        print(0)

