<?php
class FileHandler
{
    private $file;
    public function __construct($file)
    {
        if (!is_file($file)) {
            throw new RuntimeException("不是有效的文件：{$file}");
        }

        if (!is_readable($file)) {
            throw new RuntimeException("文件不可读取：{$file}");
        }

        if (!is_writable($file)) {
            throw new RuntimeException("文件不可写入：{$file}");
        }

        $this->file = $file;
    }
    public function read()
    {
        $content = file_get_contents($this->file);
        if ($content === false) {
            throw new RuntimeException("读取文件失败：{$this->file}");
        }
        return $content;
    }
    public function write($data)
    {
        $result = file_put_contents($this->file, $data);
        if ($result === false) {
            throw new RuntimeException("写入文件失败：{$this->file}");
        }
        echo "写入成功\n";
    }
}
$text = <<<EOF
How it works?
EOF;
try {
    $file = new FileHandler("test.txt");
    $file->write($text);
    echo $file->read();
} catch (RuntimeException $e) {
    echo $e->getMessage();
}
?>


