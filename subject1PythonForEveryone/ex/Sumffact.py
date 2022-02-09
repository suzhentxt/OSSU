k = float(input())
s = 0
gt = 1
n = 1
t = 1
while (k<=t):
	gt *= n;
	t = 1.0/gt;
	s += t;
	n += 1;
s -= t;
print(round(s,9));
#sai 1 test