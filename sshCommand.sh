#!/bin/bash
# -*- coding: utf-8 -*-

#ssh接続先で音声再生させるスクリプト
#引数として受け取ったファイル名を再生させる

USER="$1"
HOST="$2"
FILEPATH="$3"

ssh ${USER}@${HOST} "play ${FILEPATH}"

