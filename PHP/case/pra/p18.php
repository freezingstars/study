<?php
if (isset($_POST['userInput'])) {
    $file = fopen('testFile.txt', 'a');
    fwrite($file, $_POST['userInput'] . PHP_EOL);
    fclose($file);
    echo 'Write success';
} else {
    echo 'No input';
}
echo 1%2;