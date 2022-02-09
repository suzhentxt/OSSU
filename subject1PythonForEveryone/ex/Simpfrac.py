a,b = map(int,input().split())
x = a
y = b
while b != 0:
    r = a % b
    a = b
    b = r
x //= a
y //= a
print(x,y)