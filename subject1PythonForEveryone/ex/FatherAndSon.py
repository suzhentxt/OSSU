def check(x,y):
    if  (y*2) > x:
	    return -1
    else: return x-(y*2)	

t = int(input())
b = []
for i in range(1,t):
    x,y = map(int,input().split())
    b.append(check(x,y))

for i in b: print(i)


            


