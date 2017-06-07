#!/bin/bash
# -*- coding: utf-8 -*-

#引数で受け取ったホスト名に対応したIPアドレスを返す

TARGET="$1"

if [ -z "$TARGET" ]; then
	TARGET="tsubasa-server"
fi
# コマンドラインでハマチから相手先のIPアドレスを取得する
sudo hamachi list | grep ${TARGET} | sed -E 's/\ +/\n/g' | grep -E '^(([0-9]{1,3}\.){3}[0-9]{1,3})$' > ipaddress.txt

# pythonに返すためのコマンド
cat ipaddress.txt
