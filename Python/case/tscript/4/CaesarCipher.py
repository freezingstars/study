str1 = input('文本：')
print("原文：",str1)
for i in range(0,len(str1)):
    if str1[i] == " ":
        print("",end="")
    elif str1[i] in "xyz":
        print(chr(ord(str1[i])-23), end="")
    else:
        print(chr(ord(str1[i])+3), end="")