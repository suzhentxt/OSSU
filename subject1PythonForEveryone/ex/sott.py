<<<<<<< HEAD
n, m = map(int,input().split())

n2 = []
m2 = []

tam = min(n,m)

for i in range(1,tam):
    if n % i == 0: 
        n2.append(i)

for i in range(1,tam):
    if m % i == 0: 
        m2.append(i)

if n2 == m2: print(1)
else: print(0)

=======
n, m = map(int,input().split())

n2 = []
m2 = []

tam = min(n,m)

for i in range(1,tam):
    if n % i == 0: 
        n2.append(i)

for i in range(1,tam):
    if m % i == 0: 
        m2.append(i)

if n2 == m2: print(1)
else: print(0)

>>>>>>> c86c51b107c58c35667363688dc1ba559b89806d
