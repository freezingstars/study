# PHP Missing study

## 基础
### 标记与注释
标记一般使用
``` php
<?php /*代码*/ ?> #标准标记
<script language="php">/*php代码*/</script> #脚本标记
```
注释有**块注释**和**行注释**，已在上述代码进行使用

### 分隔符
没什么好说的，使用;表示代码的结束。最后一行语句可以不标记结束

### 变量
定义变量时在变量名前输入$ 
` $var = 1 #同时赋值`
输出变量的值使用echo函数
php中提供了很多**预定义变量**可以使用，例如

- $\_GET &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;获取表单以get方式提交的数据
- $\_POST&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;post提交的数据会被保存在此
- $\_REQUEST&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;get和post提交的都会保存
- $GLOBALS&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PHP中所有的全局变量
- $\_SERVER&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;服务器信息
- $\_SESSION&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session会话数据
- $\_COOKIE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cookie会话数据
- $\_ENV&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;环境信息
- $\_FILES&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;用户上传的文件信息

如果一个变量保存的值刚好是另一个变量的名字，则可快速访问，在变量前多加一个$符号

``` php
<?php
    $a = 'b';
    $b = 'bb';
    echo $a.'<br>'; 
    echo $$a #这里实际上访问的就是$($a)→$b了
?>
```

变量的传递有**值传递**和**引用传递**两种方式
值传递：将变量保存的值赋值给另一个变量保存
引用传递：传递此变量的内存地址给另一个值，使用同一个内存空间（一荣俱荣，一损俱损）
内存中分区通常有：
- 栈区：&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;程序可以操作的内存部分，（不存数据，仅运行代码），少但是快
- 代码段：&nbsp;&nbsp;&nbsp;&nbsp;存储程序中的内存部分（不执行）
- 数据段：&nbsp;&nbsp;&nbsp;&nbsp;存储普通数据（全局区和静态区）
- 堆区：&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;存储复杂数据，大但是效率低
代码的执行全过程：
1. 代码装载：从脚本文件中将代码读取出来，进行编译，将编译的结果存放到代码段（字节码）
2. 代码执行：从代码段中一行一行的执行，对于变量则是在栈区开辟一段内存存储变量名，在数据段中开辟一段内存保存变量值，调用变量时实际上是调用地址
3. 内存回收：系统回收栈区和代码段中的内存

### 常量
常量：const/constant，可以被定义，不可被改变,通常不区分大小写，但是可以区分（改变第三个参数）
PHP中有两种定义常量的方式`define('常量名'，'常量值');`和`const 常量名 = 值;`

:warning:常量不需要使用$符号，不能以数字开头，通常使用大写字母命名，命名比变量松散

:warning:Define和const定义的常量区别在于访问权限

``` php
define('PI',3.141592635);
const PII = 3;
define('q_q','cry');
echo PI;
echo constant('q_q')
```



#### 系统常量
系统定义的常量，可以直接使用，例如：
- PHP_VERSION: 	PHP版本号
- PHP_INT_SIZE:	 整形大小
- PHP_INT_MAX:        整形能表示的最大值



#### 系统魔术常量

跟随环境变化，用户无法更改

- \_\_DIR\_\_:当前执行的脚本所在绝对路径
- \_\_FILE\_\_:当前执行的脚本在电脑的绝对路径（含文件名）
- \_\_LINE\_\_:当前所属的行数
- \_\_NAMESPACE\_\_:当前所属的命名空间
- \_\_CLASS\_\_:当前所属的类
- \_\_METHOD\_\_:当前所属的方法

### 数据类型
php是弱类型语言，变量本身没有数据类型
PHP中数据分为三大类八小类
基本数据类型：4个小类（整形，浮点型，字符型，布尔型）
复合数据类型：2个小类（对象类型，数组类型）
特殊数据类型：2个小类（资源类型，空类型）

PHP中有两种类型转换方式：自动转换和强制转换。以字母开头的字符串永远为0，以数字开头的字符串取到字符为止（不会同时包含两个小数点）
``` php
<?php
    $a = 'abc1.1.1';
    $b = '1.1.1abc';
    echo (float)$a + (float)$b;
?>
```
如果想要获取数据的类型是否为指定的类型，则可使用`is_类型(变量名)`，同时还有函数`var_dump()`可以输出函数的**类型与值并换行**

- Gettype(变量名)          获取类型，得到类型对应的字符串
- Settype(变量名,类型)  设定数据类型，会直接改变数据本身



### 整形

4个字节存储数据，最大32位，PHP中默认为有符号类型（区分正负），在PHP中提供了四种整形的定义方式：十进制，二进制，八进制和十六进制

``` php 
$a = 120;    # 十进制
$b = 0b110;  # 二进制
$c = 0120;   # 八进制
$d = 0x120   # 十六进制
```

（10的）十进制转二进制则为1010，再补足成32位，就是内存中存储的样式。当然，也提供了一些函数可以进行转换

- decbin()：十转二

- decoct()：十转八

- dechex()：十转十六

  以此类推，只需要改变dec,bin,oct,hex的组合顺序就可以任意转换

### 浮点型

浮点型的定义就是'$f = 1.23; 或者'$f = 1.23e10;'，整形超过自身存储值的上限时会采用浮点型存储

尽量不使用浮点数进行精度判断，浮点型保存的数据不够精准



### 运算符

赋值运算符和C一样的+-\*/%,但是多了个‘.’,'.'就是字符串拼接
比较运算符也差不多
逻辑运算符&&,||,! (!代表条件取反)，例'$var_dump(!($b == ))'
.=为拼接赋予 
错误抑制符：在可能出错的表达式前添加@符号，例如'@(10 % 0)''
三目运算符 1 ? 2 : 3 ,1true则2，false则3，可以复合嵌套
自增与自减 $a++ $a--这类

### 计算机码

正数**三码合一**，负数左侧符号位为1，反码符号位不变，其他取反；补码为反码+1
系统中存在+0与-0
00000000
10000000 反11111111 补00000000
位运算符：

- & &nbsp;&nbsp;按位与  同真则真

- |   &nbsp;按位或   有真为真

- ~ &nbsp;&nbsp;按位非   有真则假

- ^    按位异或  同则假

- <<  按位左移 右边补0

- \>>  按位右移 左边补符号位对应内容

  负数的左移右移都需要先求补码，然后再操作，最后在求回原码



### 分支

 if

``` php
if (条件){
    事件;
}elseif{
    事件;
}
```

switch

``` php
switch(条件表达式){
    case 值:
        事件;
        break;
    case 值:
        事件;
        break;
    case 值:
        事件;
        break;
    default:
        事件;
}
```



### 循环

for while do-while foreach

可以在循环体中加入continue和break关键字，continue重循环，break跳出循环

``` php
for(条件表达式1;条件表达式2;条件表达式3){ #($i=1;$i<=10;i++)
    循环体;
}
<?php for(;;):?>
    循环体;
<?php endfor;?>
```

``` php
while(条件){ #先判后循
    循环体
}
```

``` php
do{  #先循后判
    循环体
}while(表达式);
```

循环类的替代标记符，左{可以使用冒号替代，右}可以使用end加对应的实体标记



### 常用系统函数

print()类似于echo，结构相同不是函数，返回1，一般可'echo print()'

print_r()类似于var_dump，比var_dump简单，不会输出数据类型，只有值

date()按照指定格式对时间戳进行格式化,常用的选项为Y F/m d'echo date('Y 年 m 月 d 日 H:i:s',12345678)'

time()返回当前Unix时间戳

microtime()返回Unix时间戳和微秒数

strtotime()将指定格式转为时间戳

#### 数学函数

max()    min()    rand()    mt_rand()    round()    ceil()    floor()    pow()    abs()    log()



### 文件包含

在一个PHP脚本中，将另一个PHP文件包含进来，合作完成一件事情。文件包含主要用于代码的复用，有向上索取和向下给予两种主要用法

PHP中文件包含有四种形式:Include    Include_once    Require    Require_once

都意味着是否包含；仅限包含一次，但Include是**询问**意味，只会警告；Require是**要求**必须包含

PHP中被包含的文件是单独进行编译的，如果出现语法错误，也只是到包含include语句时再报错，一个文件是可以被多次加载的，防止冗余所以加once

可以使用相对路径和绝对路径两种方式加载文件

嵌套包含：文件关联的文件关联其他文件（互乘起爆符），此时相对路径很容易出错



### 函数

Function 函数名(参数){

​	函数体;

​	返回值;

}

函数命名使用字母数字下划线，不能以数字开头，可以驼峰

匿名函数的本质是一种对象

``` php
变量名 = function(){
    函数体·
}
```





### 静态变量

static实现跨函数共享数据的变量



### 伪类

实际不存在，只是帮助理解

mixed,number



### 错误

语法错误 运行时错误 逻辑错误

系统错误 用户错误 其他错误

错误触发：运行时触发，人为触发('trigger')