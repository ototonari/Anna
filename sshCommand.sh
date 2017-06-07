#!/bin/bash
# -*- coding: utf-8 -*-

#ssh接続先で音声再生させるスクリプト
#引数として受け取ったファイル名を再生させる

USER="$1"
HOST=$(cat ipaddress.txt)
FILEPATH="$2"

ssh ${USER}@${HOST} "play ${FILEPATH}"

