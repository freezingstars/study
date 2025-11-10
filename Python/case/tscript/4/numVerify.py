num = input("学号后六位: ")
while (not num.isnumeric()) or len(num) != 6 or num[0] == '0':
    num = input("重新输入学号后六位: ")
print("位数:", len(num))
print(num[::-1])
