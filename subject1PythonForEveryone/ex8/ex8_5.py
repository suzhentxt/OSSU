<<<<<<< HEAD
fhand = open("mbox-short.txt")
count = 0
for line in fhand:
    line = line.rstrip()
    if line == "": continue 
    words = line.split()
    if words[0] !="From": continue        
    print(words[1])
    count += 1
=======
fhand = open("mbox-short.txt")
count = 0
for line in fhand:
    line = line.rstrip()
    if line == "": continue 
    words = line.split()
    if words[0] !="From": continue        
    print(words[1])
    count += 1
>>>>>>> c86c51b107c58c35667363688dc1ba559b89806d
print ("There were", count, "lines in the file with From as the first word")