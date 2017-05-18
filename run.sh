#!/bin/bash


URL="http://localhost/partytube"

if [ "$(id -u)" != "0" ]; then
	echo "This script requires root" >&2
	exit 1
fi

cd "$(dirname "$0")"

script_startup() {
	sudo bash -c "screen -mdS http_collect /home/gbear/test/get_songs_http.sh $URL"
}

a=2

script_startup2() {
	sudo ./get_songs_http.sh $URL&
	a=$!	
	echo $a
}

script_shutdown() {
	killall omxplayer
	sudo kill $a
}

if ! [ -f "./url.png" ]; then
	qrencode -o ./url.png -t PNG "$URL"
fi

trap "script_shutdown" EXIT SIGTERM
script_startup2

echo "Starting"

while [ 1 ]
do
	echo "Showing playlist"
	./show_playlist.py
	clear
	filename="$(ls -u ./output/ |grep -vie '\.JPG'$|tail -n1)"
	if [ -n "$filename" ]; then
		echo "Playing $filename"
		node tweet.js $filename
		omxplayer "./output/$filename" 2>/dev/null
		ls ./output/ |grep "$filename" |xargs -n1 -i{} mv "./output/{}" "./archive"
	fi
	
done

