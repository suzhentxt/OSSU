<<<<<<< HEAD
import math

lst = [True]*(100000000)
lst[0] = lst[1] = False
res = []
for i in range(2,int(math.sqrt(10000000))):
    if lst[i] == True:
        res.append(i)
        print(i)
        if lst[i] == True: 
            j = i*i
            while j<=10000000:
                lst[j] = False
=======
import math

lst = [True]*(100000000)
lst[0] = lst[1] = False
res = []
for i in range(2,int(math.sqrt(10000000))):
    if lst[i] == True:
        res.append(i)
        print(i)
        if lst[i] == True: 
            j = i*i
            while j<=10000000:
                lst[j] = False
>>>>>>> c86c51b107c58c35667363688dc1ba559b89806d
                j += i