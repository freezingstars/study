<?php
    $a = 'abc1.1.1';
    $b = '1.1.1abc';
    echo (float)$a + (float)$b.'<br>';
    $num = 24;
    $bin_num = Decbin($num);
    $oct_num = Decoct($num);
    $hex_num = DecHex($num);
    $bin_hex = bin2hex('10');
    echo $bin_num.'<br>';
    echo $oct_num.'<br>';
    echo $hex_num.'<br>';
    echo $bin_hex.'<br>';
    ?>