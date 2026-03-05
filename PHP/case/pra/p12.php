<?php
//$testArr = [3,2,2,1,3,5];
//print_r(array_count_values($testArr));
//echo in_array(2, $testArr);
//sort($testArr);
//print_r(array_count_values($testArr));

$testArr = [3, 2, 2, 1, 3, 5];

/* 统计数组元素出现次数 */
$countArr = array_count_values($testArr);

/* 遍历输出统计结果 */
foreach ($countArr as $key => $value) {
    echo $key . ' => ' . $value . PHP_EOL;
}

/* 判断元素是否存在 */
echo in_array(2, $testArr) ? '2 exists' . PHP_EOL : '2 not exists' . PHP_EOL;

/* 排序 */
sort($testArr);

/* 再次统计并输出 */
$countArr = array_count_values($testArr);
foreach ($countArr as $key => $value) {
    echo $key . ' => ' . $value . PHP_EOL;
}
