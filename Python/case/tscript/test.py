from os.path import split

# name="Python程序设计"
#
# print(name[0],name[2:-2],name[-1])
# a = input()
# arr1 = list(a)
# revarr1 = arr1[::-1]
# print(arr1,revarr1)
# if arr1 == revarr1:
#     print("是回文数")
# else:
#     print("不是回文数")
#

# salary = int(input())
# fit = int(input())
# prize = 1 if fit <= 10 else 2 if 10 < fit <= 20 else 3 if 20 <= fit < 30 else 4
# print(salary * (prize/100+1))
arr = []
print("输入三次值")
for i in range(3):
    arr.append(int(input("")))
print(max(arr[0],arr[1],arr[2]))
