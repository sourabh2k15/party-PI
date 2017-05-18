# party-PI

note: I have just improvised on the abandoned and old "partytube" project by ethertubes

This is a raspi powered collaborative video jukebox to make your next hosted party standout 

Make sure your pi has these installed : youtube-dl, omxplayer, nodejs

https://www.raspberrypi.org/forums/viewtopic.php?p=97710 ( youtube-dl)


"sudo apt-get install omxplayer" (omx-player)


wget http://node-arm.herokuapp.com/node_latest_armhf.deb 


sudo dpkg -i node_latest_armhf.deb   (nodejs )


sudo npm install twitter 	     ( twitter module )


End result :

The script when run successfully shows playlist for 10 seconds, plays a song from output folder , tweets about it, and when   
	done playing shifts it to archive folder. While showing the playlist it shows a QR code which when scanned opens up the 
	webpage that allows us to input youtube urls for the player to download and add to playlist. There also is included a 	      managers page which can be used to remove, shift songs in playlist   

If we are out of songs it shifts 3 played songs to output folder from archive folder to keep the party going until someone 
	adds a new youtube url to download. 
	
There always runs a background process from get_songs_http.sh that looks out for newly added youtube urls and downloads them 
	using youtube-dl, saves them as name-title, ( name of person who added song to playlist through webpage ) 
	
	

<img src="https://ethertubes.com/wp-content/uploads/partytube_playlist_small.jpg" />
 
Steps to get it working:  

1) Create a folder in your apache/nginx webserver, copy all of the files into the that folder. Also remove files in php/ to be    put directly under that folder.   
2) install python dependencies: pygame
3) make the scripts executable : sudo chmod a+x run.sh (  also with get_songs_http.sh, show_playlist.py )  
3) open a terminal and run "sudo ./run.sh " to start the script

Individual module breakdown: 

*too lazy now, will add later *

