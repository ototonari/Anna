#!/bin/bash
# -*- coding: utf-8 -*-

# $2 is nothing and done
if [ -z "$2" ];then
    exit 1
fi

# def var
FILE=$1
IPADDRESS=$2

# transfer file path
FILEPATH="file/GD-${FILE}.mp3"

# ファイル転送

MSG=`./sftp.exp ${FILEPATH} ${IPADDRESS}`

i=3
while [ "$i" -ge 1 ]
do
    if echo ${MSG}; then
        echo "transfer DONE. ${i}"
        i=0
    else
        echo "transfer Failure."
        i=$((i - 1))
    fi
done


# play at remote server
REMOTEFILEPATH="GD-${FILE}.mp3"
SSH=`./ssh.exp GD-${FILE}.mp3 ${IPADDRESS}`
echo ${SSH}
