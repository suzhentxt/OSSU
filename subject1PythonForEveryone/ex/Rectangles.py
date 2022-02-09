t = int(input())

for i in range(1,t):
    n = int(input())
    if n%2 == 0: print(-1)
    else: 
        n2 = n // 2;
        if n2 == 1: print(-1)
        else:
            n3 = n2 // 2
            list = []
            for j in range(1,n3): 
                t = n2 - j
                t *= j
                list.append(t)
            print(list)
#sai