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
php中提供了很多预定义变量可以使用，例如
- $_GET
- $_POST
- $REQUEST
- $GLOBALS
- $_SERVER
- $_SESSION
- $_COOKIE
- $_ENV
- $_FILES