<?php
function fib($n) {
    if ($n <= 2) {
        return 1;
    }
    return fib($n - 1) + fib($n - 2);
}
function fibSum($n) {
    if ($n == 1) {
        return 1;
    }
    return fib($n) + fibSum($n - 1);
}
echo fibSum(10);;