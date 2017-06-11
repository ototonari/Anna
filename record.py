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
        
    def record(self):
        try:
            os.system(self.__sox)
        except:
            raise ValueError("Recording.record is Failure.")

    def getIPaddress(self,hostname):
        try:
            subprocess.getoutput("bash ./getIPaddress.sh {}".format(hostname))
            print("getIP DONE.")
        except:
            raise ValueError("Recording.getIPaddress is Failure.")


def exData(file):
    try:
        subprocess.getoutput("bash ./exData.sh {}".format(file))
        time.sleep(2)
        print("exData DONE.")
    except:
        raise ValueError("exData is Failure.")

def getIPaddress(file):
    try:
        
        exData(file)

        f = open("hostlist", 'r', encoding='utf-8')
        
        for cnt, list in enumerate(f):
            cnt = subprocess.getoutput("bash ./getIPaddress.sh {}".format(list))
            #p = threading.Thread(target=smartFileTransfer,args=(file))
            #p.start()

            smartFileTransfer(file, cnt)

        f.close()
        #os.system("bash ./remove.sh {}".format(file))
    except:
        raise ValueError("getIPaddress is Failure.")


def smartFileTransfer(file, ipaddress):
    try:
        command = "bash ./smartFileTransfer.sh {file} {ipaddress} &".format(file=file, ipaddress=ipaddress)
        os.system(command)
    except:
        raise ValueError("smartFileTransfer is Failure.")


try:
    while True:
        rec = Recording()
        rec.record()
        #time.sleep(1)
        #exData(rec.date)
        getIPaddress(rec.date)
        time.sleep(10)

except KeyboardInterrupt:
    print("stop")


