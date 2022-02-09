hrs = float(input("Enter Hours:"))
rt = float(input("Enter Rate: "))
if hrs>40:
    tam = (hrs-40)*(rt*1.5)
    tam2 = 40*rt
    print(tam+tam2)
else: print(hrs*rt)