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

- \_\_DIR\_\_:
- \_\_FILE\_\_:
- \_\_LINE\_\_:
- \_\_NAMESPACE\_\_:
- \_\_CLASS\_\_:
- \_\_METHOD\_\_: