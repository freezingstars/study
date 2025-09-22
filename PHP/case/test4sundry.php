<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Test page 4 my PHP</title>
</head>
<body>
<h1>Just for test</h1>
<a href="https://www.baidu.com">👉有什么问题你百度啊👈</a><br>
<?php
    $num1 = 3;
    $AdminName = "Googeon";
    $str1 = "Hello user";
    const BM = "Black Math:WuKong";
    echo $str1,"($AdminName) ";
    $num2 = ++$num1;
    echo $num2.' PHPStudy'.'<br>';
    $my_info = array('name'=>'Googeon', 'age'=>22, 'hobby'=>'sleep');
    foreach($my_info as $k=>$v){
        echo $k.':'.' '.$v.'<br>';
    }
    $num_array = array(32,14,24,53,57,13,45,75);
    echo "排序前:";
    foreach($num_array as $k){
        echo $k.' ';
    }
    echo "<br>";
    echo "排序后:";
    sort($num_array); /* 在原数组上修改，不产生新数组，含有键值对时使用asort($arr)和arsort来保持键值对应,
        按键名排序用ksort和krsort*/
    foreach($num_array as $k){
        echo $k.' ';
    }
    echo "<br>";
    sort($num_array);
    $need1e_f = 'Googeon';
    $element = array_search($need1e_f, $my_info);
    echo $my_info[$element]; # 属于是脱裤子放屁，根据值查找键名，再打印出键名所对应的值
    ?>
</body>
</html>