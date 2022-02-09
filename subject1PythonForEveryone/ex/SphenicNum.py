import math

def Prime(num):
	l = list(range(2,num+1))
	for i in range(2,int(math.sqrt(num)+1)):
		for j in range (i*i, num+1, i):
			if j in l:
				l.remove(j)
	return l		
def Check(n):
    d = 0
    for i in primelist: 
        if n % i == 0:
            n //= i
            while (n != 1) and (n % i == 0):
                return 0
            d += 1
    if n != 1: 
        return 0
    else:
        if d != 3:
            return 0
        else: return 1
            

t = int(input())
primelist = Prime(1000)
#primelist = [2,3,5,7,11,13,17,19,23,27,29,31,37]
for j in range(t):
    n = int(input())
    print(Check(n))
      
    