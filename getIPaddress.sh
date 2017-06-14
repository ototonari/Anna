#!/bin/bash
# -*- coding: utf-8 -*-

#引数で受け取ったホスト名に対応したIPアドレスを返す

TARGET="$1"

if [ -z "$TARGET" ]; then
    TARGET="tsubasa-server"
fi
# コマンドラインでハマチから相手先のIPアドレスを取得する
#sudo hamachi list | grep ${TARGET} | sed -E 's/\ +/\n/g' | grep -E '^(([0-9]{1,3}\.){3}[0-9]{1,3})$'
# かつ相手が生きている場合のみ取得する
sudo hamachi list | awk '$1 ~ /^\*$/ {print}' | grep ${TARGET} | awk '{print $4}'

# pythonに返すためのコマンド
#cat ipaddress.txt
