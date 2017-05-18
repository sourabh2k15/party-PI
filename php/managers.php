<html>
<head>
	<script src="jquery.js"></script>
</head>
<body>
<?php

$playlist = "output";
$played = "archive";

$files1 = scandir($playlist);
$files2 = scandir($played);

function display($files,$flag){

	$html="<div>";	
	
	if($flag==0) $html.="<h1>Playlist</h1>";
	if($flag==1) $html.="<h1>Played</h1>";
		
	for($i=0;$i<count($files);$i++){
		if($files[$i]=="."||$files[$i]=="..") continue;
		$a = explode(".jpg",$files[$i]);
		$a = $a[0];
		if(strpos($files[$i],".jpg")>0){
			$html.="<div><span>".$a."</span>&nbsp";
			if($flag==0) $html.="<button onclick='del(this,1)'>move to played</button>&nbsp<button onclick='del(this,3)'>delete</button>";
			if($flag==1) $html.="<button onclick='del(this,2)'>move to playlist</button>&nbsp<button onclick='del(this,4)'>delete</button>";
			$html."</div>";
		}
		
	}
	$html.="</div>";
	echo $html;
}

display($files1,0);
echo"<br/>";
display($files2,1);

?>

<script>
	$(document).ready(function(){
		console.log("app ready!!");
	});
	
	function del(obj,flag){
			var fname = obj.parentNode.children[0].innerHTML;
			console.log(fname+" "+flag);
			$.ajax({
				type:"POST",
				url:"data.php",
				data:{fname:fname,flag:flag},
				success:function(data){
					console.log(data);
				},
				error:function(){
					console.log("error occurred!");
				}
			});
	}
</script>
</body>
</html>
