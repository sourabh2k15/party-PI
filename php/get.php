<?php
$file = "playlist.txt";

$contents = file_get_contents($file);
//echo $contents;
$a = explode(",",$contents);
//var_dump($a);
array_pop($a);
$url = array_shift($a);
echo $url;
$contents = implode(",",$a);
$contents.=",";
file_put_contents($file,$contents);
?>
