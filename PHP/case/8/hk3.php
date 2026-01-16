<?php
$f1 = 1;
$f2 = 1;
$sum = $f1 + $f2;
for ($i = 3; $i <= 10; $i++) {
    $tmp = $f1 + $f2;
    $sum += $tmp;
    $f1 = $f2;
    $f2 = $tmp;
}
echo "斐波那契数列前n项和：".$sum, PHP_EOL;