str1 = input("name about who president's mom is dead:")
str1 = str1.lower()
d = dict()
for c in str1:
    if c in ",. ":
        continue
    if c in d:
        d[c] = d[c] + 1
    else:
        d[c] = 1
print(sorted(d.items()))