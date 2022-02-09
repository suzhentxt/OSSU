import math

def Prime(num):
	l = list(range(2,num+1))
	for i in range(2,int(math.sqrt(num)+1)):
		for j in range (i*i, num+1, i):
			if j in l:
				l.remove(j)
	return l		

t = int(input())
primelist = Prime(100000000)

for j in range(t):
    n,k = map(int,input().split())
    b = []
    for i in primelist: 
        while (n % i == 0):
            b.append(i) 
            n //= i  
    if n != 1:  
        b.append(n) 
    if k > len(b): print(-1)
    else: print(b[k-1]) 