<?php
function my_error($errno, $errstr, $errfile, $errline) {
    if (!(error_reporting() & $errno)) {
        return false;
    }
    switch ($errno) :
        case E_ERROR:
        case E_USER_ERROR:
                echo 'Fatal error in file ' . $errfile . ' on line ' . $errline . '<br>';
                echo 'Error info: ' . $errstr;
            break;
        case E_WARNING:
        case E_USER_WARNING:
                echo 'Warning in file ' . $errfile . ' on line ' . $errline . '<br>';
                echo 'Error info: ' . $errstr;
            break;
        case E_NOTICE:
        case E_USER_NOTICE:
                echo 'Notice in file ' . $errfile . ' on line ' . $errline . '<br>';
                echo 'Error info: ' . $errstr;
            break;
    endswitch;
    return true;
}

set_error_handler('my_error');

echo $a;
?>
