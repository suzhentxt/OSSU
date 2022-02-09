<<<<<<< HEAD
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


            


=======
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


            


>>>>>>> c86c51b107c58c35667363688dc1ba559b89806d
