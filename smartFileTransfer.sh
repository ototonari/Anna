#!/bin/bash


# $2 is nothing and done
if [ -z "$2" ];then
	exit 1
fi

# def var
FILE=$1
IPADDRESS=$2
# transfer file path
FILEPATH="file/GD-${FILE}.mp3"

# def func

file_transfer ()
{
	local filepath=$1
	expect -c "
		set timeout -1
		spawn env LANG=C /usr/bin/sftp pi@${IPADDRESS}
		expect \"sftp>\ \"
		send \"put ${filepath}\n\"
		expect \"sftp>\ \"
		send \"bye\n\"
		exit 0
	"

}

# .wav conversion .mp3 and gain
#sox file/${FILE}.wav file/${FILE}.mp3 
#sox file/${FILE}.mp3 file/tmp${FILE}.mp3 gain -n
#sox file/tmp${FILE}.mp3 file/GD-${FILE}.mp3 gain -l 5

# transfer

MSG=`./expect.sh ${FILEPATH} ${IPADDRESS}`

i=3
while [ "$i" -ge 1 ]
do
#	if file_transfer "$FILEPATH"; then
	if echo ${MSG}; then
		echo "transfer DONE. ${i}"
		i=0
	else
		echo "transfer Failure."
		i=$((i - 1))
	fi
done

# local .wav .mp3 remove
#rm file/tmp${FILE}.mp3 file/${FILE}.wav file/GD-${FILE}.mp3 file/${FILE}.mp3


# play at remote server

ssh pi@${IPADDRESS} "play GD-${FILE}.mp3"

