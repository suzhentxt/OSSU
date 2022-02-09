<<<<<<< HEAD
n = int(input())
d = 0
i = 1
sum = 0
while n>0:
    sum += i
    n -= sum
    if n>=0: d += 1
    i += 1
=======
n = int(input())
d = 0
i = 1
sum = 0
while n>0:
    sum += i
    n -= sum
    if n>=0: d += 1
    i += 1
>>>>>>> c86c51b107c58c35667363688dc1ba559b89806d
print(d)