 <?php
/**
 * @param array $arr
 * @return array
 */
function array_to_unique(array $arr)#: array
{
    $result = [];
    $exists = [];

    foreach ($arr as $key => $value) {
        if (!in_array($value, $exists, true)) {
            $exists[] = $value;
            $result[$key] = $value;
        }
    }
    return $result;
}
$arr1 = [];
for ($i = 0; $i < 20; $i++) {
    $arr1[] = mt_rand(1, 10);
}
foreach ($arr1 as $key => $value) {
    echo "arr1[$key]" .'->'. $value . "\n";
}
$arr2 = array_to_unique($arr1);
print_r($arr2);
 ?>