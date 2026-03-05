<?php
for($i=0;$i<=20;$i++){
    if($i==7){
        continue;
    }elseif ($i==15){
        break;
    }
    echo $i;
}