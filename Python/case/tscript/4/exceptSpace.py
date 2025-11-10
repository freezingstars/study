s = input("字符串：")
i = 0
while i < len(s) and s[i] == " ":
    i += 1
j = len(s)-1
while j >=0 and s[i] == " ":
    j -= 1
print(s[i:j+1])