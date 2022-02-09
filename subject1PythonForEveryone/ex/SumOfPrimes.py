import math

n = 100000
a = []
for i in range(100000): a.append(0)
#print(a)
i = 1 
a[i] = 1
j = 1
for i in range(2,int(math.sqrt(n))):
    if a[i] == 0:
        j = i*i
        while j <= n:
            a[j] = 1
            j += i

t = int(input())
for j in range(t):
    l,r = map(int,input().split()) 
    sum = 0
    for n in range(l,r):
        ls = list(reversed(str(n)))
        n2 = ''.join(ls)
        if (a[n] == 0):
            if n == (int(n2)):
                sum += n
    print(sum)
#sai 


