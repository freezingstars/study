<?php
    if ($_SERVER['REQUEST_METHOD'] == 'POST')
    {
        $username = $_POST["username"];
        $pwd = $_POST["password"];

        function verification($username, $pwd)
        {
            $xml = simplexml_load_file('users.xml') or die("加载 XML 文件失败");
            foreach ($xml->children() as $user) {
                if ((string)$user->username === $username && (string)$user->password === $pwd) {
                    return 1;
                }
            }
            return 0;
        }

        if (verification($username, $pwd) == 1) {
            echo "登录验证通过";
        } else {
            echo "登录失败";
        }
    }else{
        header("Location: login.html");
        exit;
    }
?>