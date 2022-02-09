n = int(input())
s = input()
s2 = s.split()
a = [int(i) for i in s2]
d = 0
for i in a:
    if i == 1: d -= 1   
    else: d += 1
print(abs(d))
