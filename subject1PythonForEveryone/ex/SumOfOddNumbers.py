n = int(input())
str = input()
list = str.split()
lnum = [int(i) for i in list]
t = 0
for i in lnum:
    if i%2!=0:
        t += i
print(t)