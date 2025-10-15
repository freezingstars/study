num = int(input("请输入一个数："))
sum = 0
x = 10
id = 0
empty_arr = []
temp = num
while temp > 0:
    empty_arr.append(temp % x)
    temp //= 10
for i in empty_arr:
    sum += pow(i, 3)
if sum == num:
    print(num, '是水仙花数')
else:
    print(num, '不是水仙花数')
