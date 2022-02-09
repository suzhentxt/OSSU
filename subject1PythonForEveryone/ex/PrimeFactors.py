t = int(input())
for z in range(t):
    n = int(input())
    i = 2
    ls = []
    while n != 1:
        if n % i == 0:
            d = 0
            while (n != 1) and (n % i == 0):
                n //= i
                d += 1
            ls.append(str(i))
            ls.append(str(d))
        else: i += 1
    print(" ".join(ls))


