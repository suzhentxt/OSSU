import math
def is_prime(n):
    if n <= 1:
        return False
    if n in [2,3,5,7]:
        return True
    if (n % 2 == 0) or (n % 3 == 0) or (n % 5 == 0) or (n % 7 == 0):
        return False
    i = 5
    while (i*i) <= n:
        if (n % i == 0) and (n % (i + 2) == 0):
            return False
        else:
            i+=6
    return (i*i > n)

"""for i in range(2,50):
    if is_prime(i):
        print(i)
"""
t = int(input())

for i in range(t):
    n = int(input())
    s = n // 2 + 1
    i = s
    d = 0
    maxx = 0 
    list = []
    if is_prime(n): print(n)
    else: 
        while (i >= 2):
            if n % i == 0:
                if is_prime(i) == True:
                    while (n != 1) and (n % i == 0): n //= i
                    j = n//i
                    maxx = max(maxx,i)
                    if is_prime(j) == True: maxx = max(maxx,j)
                    #print(i,j)
                    #break
                    print(i,j)
            i -= 1
        print(maxx)