n = int(input())
str = input()
list = str.split()
lnum = [int(i) for i in list]
t = 0
for i in lnum:
    t += i
print(t)