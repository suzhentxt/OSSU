def how_many(Dict):
    result = 0
    for key in Dict.keys():
        result += len(Dict[key])
    return result