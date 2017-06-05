#!/bin/bash

#このスクリプトは引数として受け取ったファイル名を
#Hamachi内にある TARGET のホストに送信します
#前提条件として、Hamachiで同一ネットワークであること
#相手との公開鍵認証が可能であることです。

IPADDRESS=0.0.0.0
TARGET=tsubasa-server
FILEPATH="$1"

# コマンドラインでハマチから相手先のIPアドレスを取得する
sudo hamachi list | grep ${TARGET} | sed -E 's/\ +/\n/g' | grep -E '^(([0-9]{1,3}\.){3}[0-9]{1,3})$' > ipaddress.txt

IPADDRESS=$(cat ipaddress.txt)

echo "HOST:${TARGET} IP:${IPADDRESS}"

expect -c "
	set timeout 10
	spawn env LANG=C /usr/bin/sftp pi@${IPADDRESS}
	expect \"sftp>\ \"
	send \"put ${FILEPATH}\n\"
	expect \"sftp>\ \"
	send \"bye\n\"
	exit 0
"
