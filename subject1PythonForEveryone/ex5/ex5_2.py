<<<<<<< HEAD
num = 0
largest = -1
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try :
        numb = int(num)
    except :
        print('Invalid input')
    if smallest is None :
        smallest = numb
    elif numb < smallest :
        smallest = numb
    elif numb > largest :
        largest = numb
print("Maximum is", largest)
=======
num = 0
largest = -1
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try :
        numb = int(num)
    except :
        print('Invalid input')
    if smallest is None :
        smallest = numb
    elif numb < smallest :
        smallest = numb
    elif numb > largest :
        largest = numb
print("Maximum is", largest)
>>>>>>> c86c51b107c58c35667363688dc1ba559b89806d
print("Minimum is", smallest)