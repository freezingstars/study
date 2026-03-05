<?php
$str = "Learning PHP is FUN";
$pos = stripos($str, 'php');
echo $pos !== false ? $pos : "not found";
echo str_replace("PHP","PYTHON",$str) . PHP_EOL;
echo strlen(trim($str)).PHP_EOL;
print_r(explode(",","php,linux,nginx,mysql"));
echo implode(' ',["PHP","is","powerful"]);