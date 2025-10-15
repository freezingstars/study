<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST["username"];
    $pwd = $_POST["password"];
    if (file_exists('users.xml')) {
        $xml = simplexml_load_file('users.xml') or die("<script>alert('加载用户文件失败');</script>");
    } else {
        $xml = new SimpleXMLElement('<users></users>');
    }
    foreach ($xml->children() as $user) {
        if ((string)$user->username === $username) {
            echo "<script>alert('注册失败：用户名已存在');</script>";
            exit;
        }
    }
    $newUser = $xml->addChild('user');
    $newUser->addChild('username', $username);
    $newUser->addChild('password', $pwd);
    if($xml->asXML('users.xml')) {
        echo "<script>alert('注册成功！');</script>";
    } else {
        echo "<script>alert('注册失败：保存文件出错');</script>";
    }

} else {
    header("Location: register.html");
    exit;
}
?>
