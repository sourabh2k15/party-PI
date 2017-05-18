#!/bin/bash

html_decode () {
    html_encoded="$1"
    html_encoded=${html_encoded//&#/ }
    html_encoded=(`echo $html_encoded`)
    for html_dec in ${html_encoded[@]}
    do
        html_dec="${html_dec//X/x}"
        html_dec="${html_dec//;/}"
        if [ "${html_dec:0:1}" == "x" ]; then
            html_hex=${html_hex:1:${#html_hex}}
        else
            html_hex="`printf "%02X\n" $html_dec`"
        fi
        echo -en "\x$html_hex"
    done
    echo ""
}

if [ -z "$1" ]; then
	echo "Usage: $0 <Youtube ID>" >&2
	exit 1
fi
url=$1
curl -s "$url" |while read line
do
	if [ "${line//'<title>'}" != "$line" ]; then
		line="${line##*'<title>'}"
		line="${line%%'</title>'*}"
		line="${line//' - YouTube'}"
#		line="$(html_decode "$line")"
		echo "$line"
		break
	fi
done
