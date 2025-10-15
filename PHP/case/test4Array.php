<?php
$info = array(
    array('stuname' => 'Jack', 'age' => 21),
    array('stuname' => 'Jerry', 'age' => 22),
    array('stuname' => 'Tom', 'age' => 23)
);

print_r($info);

foreach ($info as $student) {
    echo 'name: ' . $student['stuname'] . ', age: ' . $student['age'] . '<br>';
}
?>
