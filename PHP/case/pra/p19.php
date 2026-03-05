<?php
$json = '{"name":"Tom","age":18}';

$a = json_decode($json);      // 对象
$b = json_decode($json, true); // 数组

echo $a->name;
echo $a->age;
echo $b['name'];
echo $b['age'];
print_r(var_dump($a));
echo <<<EOF
Sometime you should have a relax rest.
EOF;
