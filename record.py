#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 録音するスクリプト
# 実行ディレクトリに file のサブディレクトリが必要

import time
import os
import datetime
import subprocess
import threading

# 録音ファイル生成用クラス
class Recording:
    def __init__(self):
        self.__PATH = "file/"
        #録音開始時の年月日と時分を取得したファイル名
        self.date = "{:%Y-%m%d-%H:%M}".format(datetime.datetime.now())
        self.__recFile = self.date + ".wav"
        #録音開始のシェルスクリプト
        self.__sox = "sox -c 2 -d {dir}{file} silence 1 00:00:00.5 0.2% 1 00:00:10 2%".format(dir=self.__PATH,file=self.__recFile)
    
    # mainメソッド
    def record(self):
        try:
            os.system(self.__sox)
        except:
            raise ValueError("Recording.record is Failure.")

# 音量調節とファイル形式を変換する
def exData(file):
    try:
        subprocess.getoutput("bash ./exData.sh {}".format(file))
        time.sleep(2)
        print("exData DONE.")
    except:
        raise ValueError("exData is Failure.")

# 作業ディレクトリにあるhostlistを読み込みhamachi list からIPアドレスを割り出し、smartFileTransfer.sh にデータ名とIPを渡す
def getIPaddress(file):
    try:
        
        exData(file)

        # hostlist 内のホスト名を1行ずつ読み取り、smartFileTransfer.sh に渡す
        f = open("hostlist", 'r', encoding='utf-8')
        for cnt, list in enumerate(f):
            cnt = subprocess.getoutput("bash ./getIPaddress.sh {}".format(list))
            smartFileTransfer(file, cnt)

        f.close()
        os.system("bash ./remove.sh {}".format(file))
    except:
        raise ValueError("getIPaddress is Failure.")

# ファイル名とIPアドレスを受け取り、sftpでデータ送信後、sshで再生を指示する。
def smartFileTransfer(file, ipaddress):
    try:
        command = "bash ./smartFileTransfer.sh {file} {ipaddress} &".format(file=file, ipaddress=ipaddress)
        os.system(command)
    except:
        raise ValueError("smartFileTransfer is Failure.")

# メイン処理 time.sleep(3)は処理を中断させるための間
try:
    while True:
        rec = Recording()
        rec.record()
        getIPaddress(rec.date)
        time.sleep(3)

except KeyboardInterrupt:
    print("stop")


