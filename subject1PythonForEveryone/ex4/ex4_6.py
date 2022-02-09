def computepay(h, r):
    if hrs>40:
   		t = (hrs-40)*(rate*1.5)
    else: t = 0
    t2 = 40*rate
    return t+t2

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate: "))
p = computepay(hrs, rate)
print("Pay", p)