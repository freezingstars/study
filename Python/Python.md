# 基础
## 值类型
### 字面量
数值 	int float complex bool
字符串 	string
列表		list		有序可变序列
元组 	Tuple		有序不可变序列
集合 	Set			无序不重复集合
字典 	Dictionary	无序key—value集合

### 注释
\# 单行注释
""" 多行注释，开头结尾都是三个引号

### 变量
存储计算结果或表示值的抽象概念
```python
变量名称 = 变量值
```
```java
变量类型 变量名称 = 变量值;
```
Python中的赋值无需声明变量的类型，变量无类型，但是数据有

### 查看数据类型
函数type()可以查看数据类型，也可以进行类型储存
```python
print(type(你想查看的变量/字面量))
```

### 数据类型转换
``` python
数据类型(变量)
```

### 标识符
用户编程时使用的一系列命名
1.标识符命名中仅可
	- 英文
	- 中文（不建议）
	- 数字（不可用以开头）
	- 下划线
	2.大小写敏感（区分）
	3.不可使用关键字

### 运算符
|符号|用途|
|:--:|:--:|
|\+|加|
|\-|减|
|\*|乘|
|/|除|
|//|取整除（只取整数部分）|
|%|取余|
|\*\*|指数(幂)|

## 字符串
### 定义
可以单引号 双引号 三引号
``` python
HW = """Hello world!"""
"""Hello world!"""
HW1 = """
Hello
user
Googeon·Willam
"""
```
如果不使用变量接收三引号字符串，则视作注释
同时三引号中的内容会被隔行保留，输出结果包括换行的内容

### 字符串拼接
字符串拼接可以使用+号,如果是其他类型，需要转义str后或者使用','隔开
```python
HW = "Hello world"
print(HW+"from Pycharm")
```

### 字符串格式化
可以在字符串中加入%进行占位拼接,%s表示将拼接所用的值转为str
``` python
h = "hello"
w = "world"
user1 = "Googeon"
print("%s %s\n%s %s" % (h, w, h, user1))
```
- %s 	字符型转换
- %d 	整形转换
- %f 	浮点型转换
- %5.2f 将浮点型宽度控制为5，小数点精度为2
``` python 
num = 12.3456
print("%7.3f" % num) # 输出结果为  12.346 ← 取整为6，算是精度损失
# 因为位数控制为7，结果未达到7位，所以增添1个空位在前
# python不会进行截断，所以即使位数控制在6以下输出也是12.346，也可以直接%.3f
```

字符串格式化仍有其他写法
```python
num = 12.3456
print(f"数值num：{num}") #此时f表示format，无关类型与精度控制
```

如欲将表达式写入字符串中，可：
``` python
print("1.2 * 3.4的结果为：%4.2f，类型为%s" % (1.2*3.4,type(1.2*3.4)))
```

### 数据输入/出
input()/print()
``` python
name = input()
```
input接收的值会被转为字符型,可以通过int(input("整形转换："))将输入的值转为整形

## 判断
### 布尔类
布尔(bool)，对于这个函数只会输出两个结果（true，false）同时也是1真，0假，也可以进行手动定义true/false
``` python
result = 0.8 > 0.11
print(f"0.8>0.11的结果为{result}，类型为{type{result}}")
```
比较运算符有
== != > < >= <=

### 循环
#### if语句
python中的判断语句并无{}()这类代码块的开始与结束符号，而是通过缩进判断代码块的开始与结束
```python
age = 22
if age > 18:
	print("已成年")

```

##### if else
``` python
"""if 条件：
	条件成立
else：
	条件失败"""
age = int(input("输入你的年龄："))
if 100 > age > 18:
    print("已成年")
elif age == 18:
    print("刚好成年")
elif 0 < age < 18:
    print("未成年")
else:
    print("捣乱的叉出去")
```

#### while
```python
"""
while 条件：
	条件成立时的事件1
	条件成立时的事件2
	条件成立时的事件3
"""
i, result = 1, 0
while i <= 100:
    result += i
    i += 1
    #while i <= 100: result, i = result + i, i + 1 可以通过，分隔行，但仍在一个代码块内
print(result)

```

#### for
``` python
# for 临时变量 in 条件循环:
# 	成立事件
testText = """
The past is a foreign country:
they do things differently there.
"""
count = 0
for i in testText:
	if i == "t":
		count += 1
print(f"文章内共有{count}个t")
```
python中for循环为轮询，无法定义循环条件，仅能从被处理的数据集中依次取出内容进行处理。无法构筑无限循环。

#### range
range(num),表示获取一个从0开始，到num结束的数字序列，并不包含num本身。也可以认为是获取从0开始，步长为num的递增数字序列
range(num1,num2),表示获取一个从num1开始，到num2结束的数字序列，依旧不包含num2本身
range(num1,num2,step)获得一个从num1开始，到num2结束的数字序列，不包含num2本身，数字间的步长以step为准（默认为1），例如range(5,10,2)取得的数据是（5,7,9）
``` python
addResult = 0
for x in range(10):
	addResult += x
print(addResult)
```

#### 变量作用域
按理在代码块内定义的变量，离开代码块后就会被立刻销毁，但是在python中不会
代码规范上不允许，但实际可以

#### 乘法表实例
``` python
for a in range(1,9):
	for b in range(1,a+1):
		print(f"{a}x{b}={a*b}\t", end='') #end=‘’将尾部自带的换行符去除
	print()
```

#### continue,break
continue 	打断并进入下一轮循环
break    	跳出循环

random.randint(a,b)随机数函数，从a至b

## 函数
预制代码块，可重复使用
例如len() input() random
也可以自己定义一个函数:
``` python
str1 = "We laughed and kept saying 'see you soon', but inside we both knew we'd never see each other again."
str2 = "I was within and without,simultaneously enchanted and repelled by the inexhaustible variety of life."
str3 = "You never really know a man until you stand in his shoes and walk around in them."
def my_len(data):
	count = 0
	for i in data:
		count += 1
	print(f"字符串{data}的长度是{count}")
my_len(str1)
my_len(str2)
my_len(str3)
```

### 定义
函数的定义为：
``` python
def 函数名(传入的参数):
	函数体
	return 返回值
```
函数必须先定义后使用，返回值可以被省略

### 函数的参数
传参：接受外部（调用）时提供的数据
可以动态的处理变量数据，而非固定，传入的参数数量也可以任意
``` python
def add(a,b):
	# return int(a)+int(b)
	result = int(a)+int(b)
	return result
	print("此处并不会被输出")
print(add(input(),input()))
```
python中有None类型，表示空的，无意义的，这也是函数的默认返回值
当省略return的值时，返回的内容就是NoneType类型
``` python
def noneTest():
	print("Hello world")
	# return None
result = noneTest()
print(f"返回值：{result}，返回类型：{type(result)}")
```

### 作用域
局部变量和全局变量的生命周期与Java和C一样，局部变量离开代码块立刻销毁
但可以通过使用关键字globe将代码块内部的变量变为全局变量
``` python
num = 2
def testNum():
    num = 5
    global num1 #一般建议在代码块外部先定义一次num1
    num1 = 3
    print(num)
testNum()
print(num1)
print(num)
```

## 数据容器
一种可以容纳多份数据的数据类型，容纳的每一份数据称之为一个元素
每一个元素可以是任意类型的数据
数据容器根据特点的不同（是否重复，是否可修改，是否有序）分为五类：
列表list，元组tuple，字符串str，集合set，字典dict
### list
``` python
# 字面量
[元素1，元素2，元素3]
# 定义变量
变量名 = [元素1，元素2，元素3]
# 定义空列表
变量名 = []
变量名 = list()
```
列表可以嵌套，下标从0开始，也可以反向索引，从右向左，初始下标为-1
例如
``` python
testList = [1,2,3,4,5]
print(testList[0])
print(testList[-1])
```
数组嵌套可称为多维数组，例如二维数组:
``` python
testList = [[1,2,3],[4,5,6],[7,8,9]]
print(testList[0][0])
print(testList[1][-2])
print(testList[-1][-1])
```

#### 列表操作
Python中如果函数定义为class（类）的成员，便称之为方法
方法的生命周期与类相同，调用的方式也不一样
例如
``` python
class Test:
	def add(self,x,y): #self用于访问实例属性和实例方法
		return x+y
test = Test() # 令实例test传递自身内存地址，创建对象
print(test.add(1,2))
# class Test:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def add(self,x,y):
#         return x+y
# tAdd = Test(2,3)
# print(tAdd.add(1,2))
```

列表.index(元素) 			列表查询，查找指定元素的下标
列表[下标] = 值 			列表修改（重赋值）
列表.insert(下标，元素)	在指定的下标位置插入元素，后续元素下标+1
列表.append(元素)			在表尾增添元素
列表.extend([元素，元素])	扩充列表
del 列表[下标]			删除指定下标元素
列表.pop(下标)			取出一个元素（剪切）
列表.remove(元素)			删去在列表中的第一个匹配项
列表.clear				清空列表
列表.count（元素）		统计指定元素在列表中的数量

#### 列表遍历
``` python
list1 = [1,2,3,4]
index = 0
while index < len(list1): # 下标<列表长度
    element = list1[index]
    index += 1
    print(element, end=" ")

list2 = [5,6,7,8]
for i in list2:
    print(i, end=" ")
```
while可以自定义循环条件，也可以实现无限循环
for单纯遍历

### 元组
元组是一组无法被篡改的“原始数据”，如果希望封装数据又不希望数据被篡改，元组无疑是最合适的
``` py
#元组字面量
(元素1，元素2，元素3)
#定义元组变量
变量名 = (元素1，元素2，元素3)
#定义空元组
变量名 = ()
变量名 = tuple()
```
 如果元组中只有一个元素，则仍需要在元素后添加括号，否则便不是元组（自动转换），也可以认为括号只是一种运算符，而逗号是元组的判别符号
 元组的操作可以参考list，例如二维元组[0][1]元组也可以嵌套
 仅有index count len可用
 虽然元组内容不可修改，但是如果元组内嵌套了一个list，则嵌套的list可以被修改，例如
 ``` py
# stuDate = ("name","age","class")
# stu1 = ["小明",21,5]
# stuList = list(zip(stuDate,stu1)) #zip可以将两个列表关联在一起
# for a, n in enumerate(stuList): #enumerate可以同时输出元组的索引和元素
#     if 21 in n:
#         print("索引：",a,"元素：",n)
stu1 = ("小明", [21], 3) #此处下标为1的元素是一个列表，21是这个列表中下标为0的元素
stu1[1][0] += 1
print(stu1)
 ```

### 字符串
字符串也是一种数据容器，可以存放任意数量的字符
字符串无法修改，查找（index），取长（len），替换（replace），分隔（split），剥离（strip）
 ``` py
str1 = "Happiness in this world, when it comes, comes incidentally. Make it the object of pursuit, and it leads us a wild-goose chase, and is never attained."
print(str1[3],str1[34])
str2 = str1.replace("incidentally","suddenly")
print(str2)
 ```
字符串的替换可以使用replace，实际上是用函数生成了一个新的字符串，新字符串也是replace的返回值

通过.split将一个字符串分割为多个字符串并存入一个列表对象内
``` py
#字符串.split(分隔符)
str1 = "There is a skeleton in every house."
str_list = str1.split(" ")#以空格为分隔符
print(str_list)
```

strip可以剥离头尾的指定字符，如果不指定参数，则默认剥离头尾的空格
``` py
str1 = "  12he11o wor1d21  "
str2 = str1.strip()
str3 = str2.strip("21") #实际为在头尾分别去除相邻的元素1和2
print(str3) #输出为he11o wor1d
```

### 序列
内容连续，有序，可以使用下标索引的一类数据容器
列表，元组，字符串都可以是序列。序列支持切片操作，按条件取出其中的一段数据
序列[起始下标:结束下标:步长],取出的结果不包括结束下标且不影响序列本身，只是得到一串新的字符串
``` py
list1 = [0,1,2,3,4,5,6,7,8]
result1 = list1[1:9:2] #不写步长默认为1,负数则为反向取值
result2 = list1[::2]
result3 = list1[::-1]
list1.reverse() #修改原序列且不返回新对象
print(result1)
print(result2)
print(result3)
print(list1) 
```

### 集合
集合最主要的特点就是不重复且无序，因为无序，所以下标索引无法访问。想遍历其中的元素需要使用for循环
``` py
# 集合字面量
{元素，元素，元素，元素}
# 定义集合变量
变量名 = {元素，元素，元素，元素}
# 定义空集合
变量名 = set()
```
集合使用.add(元素)来添加新元素，.remove(元素)移除元素，.pop(元素)随机取出一个元素，同时修改集合，.clear()清空集合（返回一个set()表示空集合）

集合中可以通过 集合1.difference(集合2) 取差集，返回一个不同时存在于两个集合中的元素的集合，也可以认为是取非
集合1.difference_update(集合2) 在集合1的内部删除与集合2相同的元素，其实也就是在集合1中删除与集合2的交集元素
``` py
set1 = {1,2,3}
set2 = {2,3,4}
set1.difference_update(set2)
print(set1)
print(set2)
```

集合中可以通过 集合1.union(集合2) 合并组成一个新的集合，因为不重复的特性，所以也可以认为是返回了两个集合的并集

### 字典
字典的定义同样使用{},存储的数据是键值对
``` py
# 字面量
{key: value, key: value, key:value}
# 定义字典变量
my_dict = {key: value, key: value, key:value}
stu_dict = {
	"stu1": {
		"class1": 71,
		"class2": 82,
		"class3": 93
	},
	"stu2": {
		"class1": 74,
		"class2": 85,
		"class3": 96
	},
	"stu3": {
		"class1": 77,
		"class2": 88,
		"class3": 99
	}
}
# 定义空字典
my_dict = {}
my_dict = dict{}
```
字典的查找可以只 通过 键 查找 值，例如
变量名 = ["键1"]["键2"]
字典里的key不可以重复，新增和更新可以通过：
字典名["键"] = 值    			非常的简单粗暴，如果键重复了就是更新，没重复就是新增
取出（删除）元素：
变量名 = 字典名.pop[key]		并没有提供单独的函数删除元素
清空元素:
字典名.clear
获取字典所有的键：
变量名 = 字典名.keys() 
得到全部的键后可以再通过print输出
遍历字典：
``` py
stu_dict = {
	"stu1": {
		"class1": 71,
		"class2": 82,
		"class3": 93
	},
	"stu2": {
		"class1": 74,
		"class2": 85,
		"class3": 96
	},
	"stu3": {
		"class1": 77,
		"class2": 88,
		"class3": 99
	}
}
key = stu_dict.keys()
print(key)
for key in stu_dict.keys():
    print(key)
    print(stu_dict[key])
print(len(stu_dict)) #计算字典内元素数量
```

