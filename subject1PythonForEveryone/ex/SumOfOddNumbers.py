<<<<<<< HEAD
n = int(input())
str = input()
list = str.split()
lnum = [int(i) for i in list]
t = 0
for i in lnum:
    if i%2!=0:
        t += i
=======
n = int(input())
str = input()
list = str.split()
lnum = [int(i) for i in list]
t = 0
for i in lnum:
    if i%2!=0:
        t += i
>>>>>>> c86c51b107c58c35667363688dc1ba559b89806d
print(t)