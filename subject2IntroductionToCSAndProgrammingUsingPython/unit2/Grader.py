import math
def polysum(n,s):
    def area(n,s):
        a = (0.25 * n * s ** 2)/math.tan(math.pi/n)
        return a
    def perimeter(n,s):
        p = n * s
        return p
    sum = area(n,s) + (perimeter(n,s) ** 2)
    return round(sum,4)