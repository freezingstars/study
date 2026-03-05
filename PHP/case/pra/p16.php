<?php
$arr = [4,6,7,8,1,2,2,3,3,4];
print_r(array_unique($arr));
print_r(array_count_values($arr));
print_r(sort($arr).PHP_EOL);
echo in_array(10, $arr) ? 'yes' : 'no';