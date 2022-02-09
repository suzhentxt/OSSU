<<<<<<< HEAD
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    return gcdRecur(b, a % b)

x,y = map(int,input().split())
=======
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    return gcdRecur(b, a % b)

x,y = map(int,input().split())
>>>>>>> c86c51b107c58c35667363688dc1ba559b89806d
print(gcdRecur(x,y))