def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if (n % 2 == 0) or (n % 3 == 0):
        return False
    i = 5
    while (i*i) <= n:
        if (n % i == 0) and (n % (i + 2) == 0):
            return False
        else:
            i+=6
    return True

def ptich(n,k):
    i = 2  
    d = k
    while n != 1:
        if n % i == 0:
            while (n != 1) and (n % i == 0):
                d -= 1
                n //= i
                if d == 0:
                    return i
        else: i += 1
    return -1
    

t = int(input())

for j in range(t):
    n,k = map(int,input().split())
    print(ptich(n,k))

#11/20