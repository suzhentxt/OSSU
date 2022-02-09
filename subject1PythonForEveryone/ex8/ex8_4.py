<<<<<<< HEAD
fname = input("Enter file name: ")
fh = open(fname)
lst = list()                       
for line in fh:                    
    word = line.rstrip().split()    
    for element in word:           
        if element in lst:        
            continue               
        else :                     
            lst.append(element)    
lst.sort()                         
=======
fname = input("Enter file name: ")
fh = open(fname)
lst = list()                       
for line in fh:                    
    word = line.rstrip().split()    
    for element in word:           
        if element in lst:        
            continue               
        else :                     
            lst.append(element)    
lst.sort()                         
>>>>>>> c86c51b107c58c35667363688dc1ba559b89806d
print(lst)                       