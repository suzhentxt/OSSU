<<<<<<< HEAD
a,b = map(int,input().split())
x = a
y = b
while b != 0:
    r = a % b
    a = b
    b = r
=======
a,b = map(int,input().split())
x = a
y = b
while b != 0:
    r = a % b
    a = b
    b = r
>>>>>>> c86c51b107c58c35667363688dc1ba559b89806d
print(x*y//a)