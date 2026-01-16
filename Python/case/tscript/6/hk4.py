with open('.\\test\\testE.txt', encoding='utf-8') as f:
    str1 = f.read().lower()

d = dict()
for c in str1:
    if c.isalpha():
        d[c] = d.get(c, 0) + 1

sorted_d = sorted(d.items())
for key, value in sorted_d:
    print(f"{key}:{value}", end='\t')
