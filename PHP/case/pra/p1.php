<?php
//题目 1（变量 / 类型）
//要求：
//定义一个字符串 "100" 和一个整数 100
//必须使用：var_dump()
//输出二者 == 和 === 的比较结果
$char1 = '100';
$int1 = 100;
$ra = $char1==$int1;
$rb = $char1===$int1;
var_dump($ra,$rb);
echo $ra,$rb,PHP_EOL;