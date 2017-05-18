<?php
        $fname = stripslashes($_POST["fname"]);
        $flag = $_POST["flag"];

        $queue = "./output";
        $played = "./archive";
        
        if($flag==1){
                $a = rename($queue."/".$fname,$played."/".$fname);
                $b = rename($queue."/".$fname.".jpg",$played."/".$fname.".jpg");
                if($a) echo "done moving ";
                else echo "failed moving from output to archive";
        }else if($flag==2){
                $a = rename($played."/".$fname,$queue."/".$fname);
                $b = rename($played."/".$fname.".jpg",$queue."/".$fname.".jpg");
                if($a) echo "done moving ";
                else echo "failed moving from archive to output";
        }
        else if($flag==3){
                echo "flag is 3";
                 unlink($queue."/".$fname);
                unlink($queue."/".$fname.".jpg");
        }
       else if($flag==4){
                echo "flag is 4";
                unlink($played."/".$fname);
                unlink($played."/".$fname.".jpg");
        }               
?>                                    
                                    
