#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 録音するスクリプト
# 実行ディレクトリに file のサブディレクトリが必要

import time
import os
import datetime
import commands

pwd = os.system('pwd')  #カレントディレクトリ取得

# 録音ファイル生成用クラス
class Recording:
    def __init__(self):
        self.__PATH = "file/"
        #録音開始時の年月日と時分を取得したファイル名(カプセル化)
        self.__recFile = "{:%Y-%m%d-%H:%M}".format(datetime.datetime.now()) + ".wav"
        #音量調節済みのファイル名(関数に渡す為公開する)
        self.gaindFile = "GD-" + self.__recFile
        #録音開始のシェルスクリプト
        self.__sox = "sox -c 2 -d {dir}{file} silence 1 00:00:00.5 0.2% 1 00:00:10 2%".format(dir=self.__PATH,file=self.__recFile)
        #音量調節のシェルスクリプト
        self.__gain = "sox {dir}{recFile} {dir}{gaindFile} gain -n".format(dir=self.__PATH,recFile=self.__recFile,gaindFile=self.gaindFile)
        self.filePath = self.__PATH + self.gaindFile
    def record(self):
        try:
            os.system(self.__sox)
        except:
            raise ValueError("Recording.record is Failure.")

    def gain(self):
        try:
            os.system(self.__gain)
            
        except:
            raise ValueError("Recording.gain is Failure.")

    def getIPaddress(self,hostname):
        try:
            commands.getoutput("bash ./getIPaddress.sh {}".format(hostname))
        except:
            raise ValueError("Recording.getIPaddress is Failure.")


def fileTransfer(filePath):
    try:
        command = "bash ./fileTransfer.sh {filePath}".format(filePath=filePath)
        os.system(command)
    except:
        raise ValueError("fileTransfer is Failure.")

def sshCommand(user, filePath):
    try:
        command = "bash ./sshCommand.sh {user} {filePath}".format(user=user, filePath=filePath)
        commands.getoutput(command)
    except:
        raise ValueError("record.py def sshCommand is Failure.")

try:
    while True:
        rec = Recording()
        rec.record()
        rec.gain()
        fileTransfer(rec.filePath)
        time.sleep(5)
        sshCommand("pi", rec.gaindFile)
        time.sleep(5)

except KeyboardInterrupt:
    print("stop")


