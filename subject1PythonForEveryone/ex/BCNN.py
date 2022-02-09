a,b = map(int,input().split())
x = a
y = b
while b != 0:
    r = a % b
    a = b
    b = r
print(x*y//a)