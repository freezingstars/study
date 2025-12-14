with open('.\\test\\testD.txt', 'r', encoding='utf-8') as file:
    r = file.readlines()
    for i in r:
        stripped_line = i.strip()
        if stripped_line.startswith('#'):
            continue
        else:
            print(i, end='')
