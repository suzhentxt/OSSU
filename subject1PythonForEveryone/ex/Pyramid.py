n = int(input())
d = 0
i = 1
sum = 0
while n>0:
    sum += i
    n -= sum
    if n>=0: d += 1
    i += 1
print(d)