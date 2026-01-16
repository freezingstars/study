with open('.\\test\\testD.txt', encoding='utf-8') as f:
    result = [0, '']
    for line in f:
        line_stripped = line.rstrip('\n')
        t = len(line_stripped)
        if t > result[0]:
            result = [t, line]
print(result)
