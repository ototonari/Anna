#!/bin/bash

#引数として送信するファイルのパスを受け取り、作業ディレクトリ内にあるipaddress.txt内のIPアドレス宛にファイルを送信します
#前提条件として、Hamachiで同一ネットワークであること
#相手との公開鍵認証が可能であることです。

FILEPATH="$1"

IPADDRESS=$(cat ipaddress.txt)

expect -c "
	set timeout 10
	spawn env LANG=C /usr/bin/sftp pi@${IPADDRESS}
	expect \"sftp>\ \"
	send \"put ${FILEPATH}\n\"
	expect \"sftp>\ \"
	send \"bye\n\"
	exit 0
"
