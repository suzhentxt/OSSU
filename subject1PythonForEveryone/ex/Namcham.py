n = int(input())
d = 0
a2 = 0
for i in range(n):
	a = int(input())
	if a != a2:
		a2 = a
		d += 1
print(d)

