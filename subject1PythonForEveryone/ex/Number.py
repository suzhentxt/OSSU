n = int(input())
d = 0
while n != 1:
    d += 1
    if n % 2 == 0:
        n //= 2
    else: n = 3*n+1
print(d)    