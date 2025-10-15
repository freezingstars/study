<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST["username"];
    $pwd = $_POST["password"];

    function verification($username, $pwd) {
        $xml = simplexml_load_file('users.xml') or die("加载 XML 文件失败");
        foreach ($xml->children() as $user) {
            if ((string)$user->username === $username && (string)$user->password === $pwd) {
                return true;
            }
        }
        return false;
    }

    if (verification($username, $pwd)) {
        echo "<script>alert('登录验证通过');</script>";
    } else {
        echo "<script>alert('登录失败，用户名或密码错误');</script>";
    }
} else {
    header("Location: login.html");
    exit;
}
?>
<?php
