import random
a,b = random.randint(1,100),random.randint(1,100)
if a > b:
    print(f"a:{a}更大")
elif a < b:
    print(f"b:{b}更大")
else:
    print("相等")