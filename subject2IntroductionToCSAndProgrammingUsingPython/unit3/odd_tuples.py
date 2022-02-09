def oddTuples(aTuple):
    rTuple = ()
    i = 0
    while i < len(aTuple):
        rTuple += (aTuple[i],)
        i += 2
    return rTuple

a = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(a))