
<?php

$url = $_POST["url"];
$name = $_POST["name"];

if (strpos($url, "youtube") == -1 || strpos($url,"youtu.be")==-1) {
        echo "Not a valid URL";
        die();
}

// to catch only the "v" part and exclude playlist details if any that could potentially fuck us up 
if(strpos($url,"&")!=-1){
	$parts = explode("&",$url);
	$url = $parts[0];
}

// handling fancy youtube shortened links :P 
if(strpos($url,"youtu.be")>-1){
	$r = explode("/",$url);
	$url = "https://youtube.com/watch?v=".$r[3];
}

$file = "playlist.txt";
$current = file_get_contents($file);
$a = explode(",",$current);

if($a[count($a)-2]!=$url){
  $current.=$url."*".$name.",";
  file_put_contents($file,$current);
}

echo "Thank you!";

?>

