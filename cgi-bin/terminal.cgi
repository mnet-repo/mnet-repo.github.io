#!/bin/sh

echo "Content-type: text/html"
echo ""

let PORT=${HTTP_HOST##*:}+1
nc -l -p ${PORT} -e ../websocket.sh </dev/null >/dev/null &
cat ../terminal.html

echo ""
echo ""
