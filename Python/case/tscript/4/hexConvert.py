num = input("学号后六位: ")
while not num.isdigit():
    num = input("规范不符，重新输入学号后六位: ")
print(bin(int(num)),oct(int(num)),hex(int(num)))