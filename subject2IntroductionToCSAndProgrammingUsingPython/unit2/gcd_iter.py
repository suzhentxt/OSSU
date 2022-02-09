<<<<<<< HEAD
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    n = min(a, b)
    while a % n != 0 or b % n != 0:
        n -= 1
    return n

x,y = map(int,input().split())
=======
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    n = min(a, b)
    while a % n != 0 or b % n != 0:
        n -= 1
    return n

x,y = map(int,input().split())
>>>>>>> c86c51b107c58c35667363688dc1ba559b89806d
print(gcdIter(x,y))