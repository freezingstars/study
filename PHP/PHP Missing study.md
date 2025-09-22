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