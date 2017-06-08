#!/bin/bash


FILE=$1

# .wav conversion .mp3 and gain
sox file/${FILE}.wav file/${FILE}.mp3 
sox file/${FILE}.mp3 file/tmp${FILE}.mp3 gain -n
sox file/tmp${FILE}.mp3 file/GD-${FILE}.mp3 gain -l 5

# transfer file path
FILEPATH="file/GD-${FILE}.mp3"

# tmp remove
rm file/tmp${FILE}.mp3 &

# transfer File
IPADDRESS=$(cat ipaddress.txt)
echo "$FILEPATH"
expect -c "
        set timeout -1
        spawn env LANG=C /usr/bin/sftp pi@${IPADDRESS}
        expect \"sftp>\ \"
        send \"put ${FILEPATH}\n\"
        expect \"sftp>\ \"
        send \"bye\n\"
        exit 0
"
