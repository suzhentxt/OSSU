n = int(input())
str = input()
list = str.split()
lnum = [int(i) for i in list]
lnum.remove(max(lnum))
print(max(lnum))
