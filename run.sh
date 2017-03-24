#!/usr/bin/env bash

# Run all services for this
python3 -m http.server &>/dev/null &
STATIC_SERVER=$!

python3 soundctrl.py &>/dev/null &
VOLUME_SERVER=$!

# Kill both processes on finish
function trapper() {
    kill $STATIC_SERVER
    kill $VOLUME_SERVER

    wait $STATIC_SERVER
    echo "http server done"

    wait $VOLUME_SERVER
    echo "volume server done"
    exit 0
}

trap "trapper" SIGINT SIGTERM

echo "Static server running on port 8000 (pid=$STATIC_SERVER)"
echo "Volume server running on port 8001 (pid=$VOLUME_SERVER)"

while true; do
    true
done
