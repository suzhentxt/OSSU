<<<<<<< HEAD
import math

lst = [True]*(100000+1)
lst[0] = lst[1] = False
j = 0
for i in range (2, int(math.sqrt(100000))+1):
    if lst[i] == True:
        for j in range(i, 100000+1):
            temp = i*j
            if temp <= 100000:
                if temp == 100000:
                    break
                lst[temp] = False
=======
import math

lst = [True]*(100000+1)
lst[0] = lst[1] = False
j = 0
for i in range (2, int(math.sqrt(100000))+1):
    if lst[i] == True:
        for j in range(i, 100000+1):
            temp = i*j
            if temp <= 100000:
                if temp == 100000:
                    break
                lst[temp] = False
>>>>>>> c86c51b107c58c35667363688dc1ba559b89806d
                j+=i