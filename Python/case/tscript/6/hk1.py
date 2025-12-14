with open('.\\test\\testA.txt','r',encoding='utf8') as file:
    strA = file.read()

with open('.\\test\\testB.txt','r',encoding='utf8') as file:
    strB = file.read()

slist = list(strA + strB)
slist.sort()
strC = ''.join(slist)

with open('.\\test\\testC.txt','w',encoding='utf8') as file:
    file.write(strC)
