<?php
class Rectangle
{
    public float $width, $height;
    const DEFAULT_COLOR = "red";
    public function __construct(float $a, float $b)
    {
        $this->width  = $a;
        $this->height = $b;
    }
    public function getArea(): float{return $this->width * $this->height;}

    public function getPerimeter(): float{return 2 * ($this->width + $this->height);}

    public function getDefaultColor(): string{return self::DEFAULT_COLOR;}

    public function __toString(): string
    {
        $area = $this->getArea();
        $perimeter = $this->getPerimeter();
        $color = self::DEFAULT_COLOR;
        return <<<EOF
宽：{$this->width}
高：{$this->height}
面积：{$area}
周长：{$perimeter}
颜色：{$color}
EOF;
    }
}
$rec = new Rectangle(3, 5);
echo $rec->getArea(), PHP_EOL;
echo $rec->getPerimeter(), PHP_EOL;
echo $rec->getDefaultColor(), PHP_EOL;
echo $rec;
