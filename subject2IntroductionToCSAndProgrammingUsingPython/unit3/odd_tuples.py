<<<<<<< HEAD
def oddTuples(aTuple):
    rTuple = ()
    i = 0
    while i < len(aTuple):
        rTuple += (aTuple[i],)
        i += 2
    return rTuple

a = ('I', 'am', 'a', 'test', 'tuple')
=======
def oddTuples(aTuple):
    rTuple = ()
    i = 0
    while i < len(aTuple):
        rTuple += (aTuple[i],)
        i += 2
    return rTuple

a = ('I', 'am', 'a', 'test', 'tuple')
>>>>>>> c86c51b107c58c35667363688dc1ba559b89806d
print(oddTuples(a))