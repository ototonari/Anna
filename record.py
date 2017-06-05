#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 録音するスクリプト
# 実行ディレクトリに file のサブディレクトリが必要

import time
import os
import datetime

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



# ファイル転送関数 ３回までトライする
def fileTransfer(filePath):
    try:
        command = "bash ./fileTransfer.sh " + filePath
        #３回トライする
        for i in range(0,2):
            #成功したらループから抜ける ここは個人的に怪しいところ。シェルスクリプト内で明示的にexitコマンドを実装する必要あり。
            if os.system(command) == 0:
                break
            time.sleep(1)
        else:
            raise ValueError("fileTransfer is Failure.")
    except:
        pass


try:
    while True:
        rec = Recording()
        rec.record()
        rec.gain()
        fileTransfer(rec.filePath)
        time.sleep(5)

except KeyboardInterrupt:
    print("stop")


