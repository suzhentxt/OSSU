<<<<<<< HEAD
def biggest(Dict):
    maxv = 0
    result = None
    for key in Dict.keys():
        if maxv<len(Dict[key]): 
            result=key
            maxv=len(Dict[key])
=======
def biggest(Dict):
    maxv = 0
    result = None
    for key in Dict.keys():
        if maxv<len(Dict[key]): 
            result=key
            maxv=len(Dict[key])
>>>>>>> c86c51b107c58c35667363688dc1ba559b89806d
    return result