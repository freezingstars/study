with open(r"./test.txt", 'w+', encoding='utf-8') as f:
    f.write("Hello world!")
    print(f.tell())
    f.seek(0)           # 将文件指针移回开头
    content = f.readline()
    print(content)
