def returnSum(myDict):
    result = 0
    for v in myDict.values():
        if isinstance(v, int):
            result += v
    return result

data = {'a': 100, 'b': '200', 'c': 300}
print('Sum:', returnSum(data))