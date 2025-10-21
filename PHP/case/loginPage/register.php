<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST["username"];
    $pwd = $_POST["password"];
    $repeatPwd = $_POST["repeatPassword"];

    if ($pwd !== $repeatPwd) {
        echo "<script>alert('两次密码不一致'); window.history.back();</script>";
        exit;
    }

    if (file_exists('users.xml')) {
        $xml = simplexml_load_file('users.xml') or die("<script>alert('加载xml失败');</script>");
    } else {
        $xml = new SimpleXMLElement('<info></info>');
    }

    foreach ($xml->children() as $user) {
        if ((string)$user->username === $username) {
            echo "<script>alert('用户名已存在'); window.history.back();</script>";
            exit;
        }
    }

    $newUser = $xml->addChild('user');
    $newUser->addChild('username', $username);
    $newUser->addChild('password', $pwd);

    $dom = new DOMDocument('1.0', 'utf-8'); // 修正构造函数
    $dom->preserveWhiteSpace = false;
    $dom->formatOutput = true;
    $dom->loadXML($xml->asXML());

    if($xml->asXML('users.xml')) {
        echo "<script>alert('注册成功！'); window.location.href='login.html';</script>";
        $dom->save('users.xml');
    } else {
        echo "<script>alert('注册失败'); window.history.back();</script>";
    }

} else {
    header("Location: register.html");
    exit;
}
?>
