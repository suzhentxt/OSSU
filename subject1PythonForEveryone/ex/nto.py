<<<<<<< HEAD
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
=======
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
>>>>>>> c86c51b107c58c35667363688dc1ba559b89806d
    return True