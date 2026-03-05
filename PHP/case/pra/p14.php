<?php
$char1 = 'The PHP is not a safe language';

/* 字符串查找 */
$pos = stripos($char1, 'php',true);
if ($pos !== false) {
    echo "Found at position: $pos" . PHP_EOL;
} else {
    echo "Not found\n";
}

/* 文件写入与读取 */
$file1 = fopen('testFile.txt', 'w+') or exit('Unable to open file!');
fwrite($file1, $char1);

/* 关键修正点：重置文件指针 */
rewind($file1);

/* 读取文件内容 */
while (!feof($file1)) {
    echo fgets($file1);
}

fclose($file1);
