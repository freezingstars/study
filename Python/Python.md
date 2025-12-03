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
|  符号  |    用途     |
| :--: | :-------: |
|  \+  |     加     |
|  \-  |     减     |
|  \*  |     乘     |
|  /   |     除     |
|  //  | 取整除（向下取整） |
|  %   |    取余     |
| \*\* |   指数(幂)   |

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

### 类型识别

| 方法        | 作用            |
| --------- | ------------- |
| isdigit() | 字符串是否**仅**为数字 |
| isalpha() | 字符串是否**仅**为字母 |
| isalnum() | 是否仅为数字+字母     |
| isspace() | 是否为空白字符       |
| islower() | 是否全小写         |
| isupper() | 是否全大写         |
| istitle() | 首字母是否大写       |
``` Python
s = input("请输入一个字符串：")

letter_count = 0
digit_count = 0

for ch in s:
    if ch.isalpha():      # 判断是否为字母
        letter_count += 1
    elif ch.isdigit():    # 判断是否为数字
        digit_count += 1

print(f"字母数量：{letter_count}")
print(f"数字数量：{digit_count}")
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
如果在函数的实参前加入\*号，则会以元组的形式接收任意个参数。如果是\*\*符号，则视为可选参数，同时以字典形式接收任意个参数
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
通过`set/tuple(原集合/列表/数组)`可以实现相互转换，转换成数组需要导入`array`模块，使用`新数组 = array.array("类型码",旧数组)`，实际上是创建了一个新的数组，两个array分别是模块array与方法array
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

'str[:]'的形式也可以从字符串中进行取字
``` pythton
str1 = 'adfgaer'
str2 = str1[:-1]
print(str2) #adfgae
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

#### 集合操作
交'&' 并'|' 补/差'-' 对称差集'^'（仅处于其中一个集合的元素） 

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
变量名 = \["键1"]\["键2"]
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

## 异常处理
try:可能出错的代码
except：异常后执行的代码
else：无异常时执行的
finally：总会执行的
``` python
try:  
    num = int(input("input a number: "))  
    print(num)  
    print(1 / num)  
# except:  
# except (ValueError, ZeroDivisionError): #仅捕获值异常与除0错误  
#     print("自定义错误")  
#     print("!" * 10)  
  
except Exception as e: #捕获异常对象，打印其具体的报错信息  
    print("↓   被捕获的报错")  
    print(e)  
  
else:  
    print("没报错就会执行这里")  
  
finally:  
    print("总会执行这一段，资源释放")
```
raise 变量 ：以异常的形式抛出字段
``` Python
# e = Exception("111")  
# raise e  
raise Exception("111")
```

## 模块
import 模块名，从首行开始写。例如import random
常用爬虫类模块：
requests
BeautifulSoup4
NumPy
Matplotlib

创建自定义模块：
``` Python
module_name = "tool"
def 功能1():
	return 0

def 功能2():
	return 0
```
使用自定义模块功能:
``` Python
import my_module:
form my_module import 功能1,功能2,module_name #导入模块中具体的某些函数/变量

print(module_name)
my_module.功能1()
```
导入模块时，自动执行一次模块内所有的代码，所以如果想要在模块内拥有一些不会再导入后被执行的代码，可以用
``` Python
if __name__ == "__main__"
	print("运行测试")
```
这种模式允许模块在被导入时不会执行某些代码，而只有在作为独立脚本运行时才会执行这些代码

## 包
在python3.3之前，一个python文件夹要被识别为包，必须包含__init__.py文件，但是建议保留，方便识别也防止版本问题。通过这个文件可以控制导入py文件的范围与初始化操作等。
	包
		 \_\_init\_\_.py
		 模块1.py
		 模块2.py
导入则是`import 包名.模块名`,也可以加入from进行简洁导入
批量导入`from 包名 import *`，批量导入需要__init__.py文件中__all__变量的支持
``` Python
__all__ = ["模块1","模块2"] #不需要写入.py后缀
```

也可以仅导入包下模块单独的功能`from 包名.模块名 import 功能`,这个功能可以通过__all__进行拓展
``` Python
module_name = "tool"
def 功能1():
	return 0

def 功能2():
	return 0
	
def 功能3():
	return 0
	
__all__ = [功能1,功能2]
```
这样在批量导入时只会导入all内的功能

## 类与对象
面向对象三大特性：**封装、继承、多态**
可以使用`__init__(self):`来进行初始化，`__del__(self)`结尾以在**程序**结束时**进行资源释放**。
``` Python
class Student:
    # 初始化属性
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 方法
    def show(self):
        print(f"姓名：{self.name}，年龄：{self.age}")
        
    def __del__(self):
	    print(f"对象 {self.name} 已被销毁")

# 创建对象
stu1 = Student("Jack", 20)
stu2 = Student("Tom", 18)
# 调用方法
stu1.show()
stu2.show()

```

| 类             | 对象           |
| ------------- | ------------ |
| 模板、设计图        | 实例、成品        |
| 定义属性和行为       | 真正拥有属性并能执行行为 |
| 类不能直接代表某一具体事物 | 对象是具体的个体     |

| 特性  | 解释        | 关键点           | 示例                |
| --- | --------- | ------------- | ----------------- |
| 封装  | 隐藏细节，提供接口 | 私有、保护、公有属性    | `__score`         |
| 继承  | 复用代码，扩展类  | `class A(B):` | Student 继承 Person |
| 多态  | 方法名相同表现不同 | 重写方法 + 统一调用接口 | `animal.speak()`  |
### 封装
封装指 **将数据（属性）和行为（方法）封装到类中，并对外隐藏内部实现细节**。  
通过封装，可以控制哪些内容对外可见、哪些是内部私有。
- 保护数据安全，避免被随意修改
- 让对象更易使用（内部复杂，外部简单）

Python 访问控制方式：

|类型|写法|含义|
|---|---|---|
|公有属性|`self.name`|外部可访问|
|保护属性|`_age`|建议内部使用，外部可访问但不推荐|
|私有属性|`__score`|外部无法直接访问（名称改写机制）|
实例：
``` Python
class Student:
    def __init__(self, name, age):
        self.name = name       # 公有
        self._age = age        # 保护
        self.__score = 100     # 私有
    
    def show(self):
        print(self.name, self._age)

stu = Student("Jack", 20)
print(stu.name)       # ✔可访问
print(stu._age)       # ✔可访问（但不推荐）
# print(stu.__score)  # ❌报错，不能直接访问
#或者print(stu._Student__score)  # ✔可访问，但一般不用
```

### 继承

继承用于 **创建新类并复用已有类的属性和方法**。  
被继承的类称为 **父类（基类）**，继承的类称为 **子类（派生类）**。
``` Python
class Person:
    def __init__(self, name):
        self.name = name
    def show(self):
        print("姓名：", self.name)

class Student(Person):
    def show(self):
        print(f"学生姓名：{self.name}")
    def study(self):
        print(f"{self.name} 正在学习。")

stu = Student("Tom")
stu.show()
stu.study()

```

### 多态
**同一个方法名，在不同对象中表现出不同的行为**。  
多态依赖继承和方法重写。
``` Python
class Animal:
    def speak(self):
        print("动物叫")

class Dog(Animal):
    def speak(self):
        print("汪汪！")

class Cat(Animal):
    def speak(self):
        print("喵喵！")

def makeSound(animal):
    animal.speak()

makeSound(Dog())   # 输出：汪汪！
makeSound(Cat())   # 输出：喵喵！
```
多态的意义
- 提高代码的扩展性和灵活性
- 新对象只需实现相同接口，无需修改原代码（符合开闭原则）

## 静态方法与类方法
实例方法必须先实例化才能通过对象调用
对于静态方法，需要添加`@staticmethod`，方法内没有`self`和`cls`参数
可以直接通过`类名.方法名()`进行调用，无需创建对象。也可以通过对象调用，但是静态方法与实例无关。
类方法和静态方法类似，通过`@classmethod`进行标识，第一个参数为`cls`。类方法直接绑定在类上，可以直接操作类本身而不需要创建实例。

静态方法和类方法都是专用于访问类属性而不能用于操作实例对象。

## 文件操作
使用函数`open(文件路径,访问模式,encoding="编码模式")`(二进制文件不用编码)函数进行文件的访问。访问模式为r/w/a,读/写/追加。在这之后跟上+可以同时进行读写，同时对于w+和a+，在文件不存在时会创建文件，w+覆盖，a+行尾追加。二进制文件需要增添一个b选项。
使用`文件对象.close()`进行关闭操作，释放内存资源。

因为可能会遗忘close，所以可以使用with语句进行更加安全的操作(自动关闭)
``` Python
with open(文件路径,访问模式,encoding="编码模式") as f:
	content = f.read()
print(f.closed) #验证状态
```

`readline()`：逐行读取，避免占用过多内存，适合大文件
`readlines()`：读取所有，将所有行作为列表元素返回，每行都是一个字符串，适合小文件
`文件对象.write(内容)`：写入文件，对于文本文件，内容必须是字符串；二进制文件则为字节串。

因为\在python表转义，所以使用下列两种方式表示路径
``` Python
f = open(r"C:\Program Files\Windows Defender\ThirdPartyNotices.txt","r",encoding="utf-8")
g = open("C:\\Program Files\\Windows Defender\\ThirdPartyNotices.txt","r",encoding="utf-8")
```

### 文件指针定位
读模式：指针在文件开头
写/追加：指针在文件末尾
`tell()`返回当前指针位置（字节）
`seek(offset,whence)`：移动指针，offset偏移量；whence：参考点：0[文件开头],1[当前位置],2[文件末尾]

## 目录操作
所有目录/文件管理操作前导入os模块（Python内置模块）

`os.rename(源路径, 目标路径)`，给文件或目录改名，也可以移动文件（本质为改路径+改名）。不支持跨盘移动。
`os.remove(路径)`，删除文件，不能删除目录
`os.mkdir(路径)`，创建一个空目录
`os.rmdir(路径)`，删除一个为空的指定目录
`os.listdir(路径)`，查看目录内容
`os.getcwd()`，查看当前工作目录
`os.path.exists()`判断路径是否存在
`os.path.isfile(路径)`，判断是否为文件
`os.path.isdir(路径)`，判断是否为目录

## **正则表达式**
一套描述字符串模式的规则，可以认为是字符串过滤器。
在python中使用正则需要导入`re`模块
`re.match(匹配模式, 字符串, flags=0)`，只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None
``` Python
Str1 = "Hello World"  
print(re.match("Hello", Str1).span())
```
`re.search(匹配模式, 字符串, flags=0)`匹配整个字符串，直到找到一个匹配。
``` Python
Str1 = "Hello World"  
print(re.search("lo", Str1).span())
```
`re.findall()`遍历整个字符串，找到所有符合规则的非重叠子串，以列表形式返回
`re.sub(匹配规则, 新内容, 原始字符串, [替换几个,默认0所有])`,替换匹配项

正则默认是**贪婪模式**，匹配尽量多可能的字符；非贪婪模式在量词后加''?''或者其他量词。非贪婪模式会以最小值进行匹配。

| 规则符号  | 含义                                  |
| ----- | ----------------------------------- |
| .     | 任意字符                                |
| []    | 可以填入一个范围，区分大小写，任意字母为[a-zA-Z]        |
| [^]   | 非，取反,不在框内的字符                        |
| \d    | 数字                                  |
| \D    | 非数字                                 |
| \s    | 空白字符                                |
| \S    | 非空白字符                               |
| \w    | 字母、数字、汉字、下划线                        |
| \W    | 匹配非单词符号                             |
| *     | 匹配前一个字符0或多次                         |
| +     | 匹配前一个字符1或多次                         |
| ?     | 0或1次                                |
| {m}   | 恰好m次                                |
| {m,n} | 至少m次，最多n次，m != n                    |
| ^...  | 以...开头的字符串                          |
| ...$  | 以...结尾的字符串                          |
| \|    | 或，多选一`re.match("(a\|b\|c)","c")`    |
| \num  | <**(\w+)**>\w</\1>,匹配一对标签，\1表示引用第一个 |
