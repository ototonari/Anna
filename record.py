#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 録音するスクリプト
# 実行ディレクトリに file のサブディレクトリが必要

import time
import os
import datetime
import subprocess
import threading
import sys
import shlex
import remove
import traceback

# 録音ファイル生成用クラス
class Recording:
    def __init__(self, startVal, endVal):
        self.__PATH = "file/"
        #録音開始時の年月日と時分を取得したファイル名
        self.date = "{:%Y-%m-%d-%H:%M:%S}".format(datetime.datetime.now())
        self.__recFile = self.date + ".wav"
        #録音開始のシェルスクリプト
        self.__sox = "sox -c 2 -d {dir}{file} silence 1 00:00:00.5 {sV}% 1 00:00:02 {eV}% 2>/dev/null".format(dir=self.__PATH,file=self.__recFile, sV=startVal, eV=endVal)
        if os.path.exists(self.__PATH) == False:
                print("make dir ./file")
                os.makedirs(self.__PATH)

    # mainメソッド
    def record(self):
        try:
            os.system(self.__sox)
            #args = shlex.split(self.__sox)
            #subprocess.run(args)
            #subprocess.run(self.__sox)
            print("record DONE.")
        except:
            remove.remove(self.date, "")

            sys.stderr.write(datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
            traceback.print_exc(file=sys.stderr)

# 音量調節とファイル形式を変換する
def exData(file):
    try:
        subprocess.getoutput("bash ./exData.sh {}".format(file))
        #time.sleep(1)
        print("exData DONE.")
    except:
        sys.stderr.write(datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
        traceback.print_exc(file=sys.stderr)

# 録音後、共有ディレクトリにデータを移動させる
def moveData(file):
    try:
        exData(file)
        
        tmpDir = "file"
        dir = 'share'
        cmd = "sudo mv {tmpDir}/GD-{file}.mp3 {dir}/GD-{file}.mp3".format(tmpDir=tmpDir, dir=dir, file=file)
        os.system(cmd)
        print("moveData DONE.")
    except:
        sys.stderr.write(datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
        traceback.print_exc(file=sys.stderr)


def upload(file):
    try:
        exData(file)
        tmpDir = "./file/"
        #cmd = "curl --upload {tmpDir}GD-{file}.mp3 `cat upload_url.private`".format(tmpDir=tmpDir, file=file)
        cmd = "curl --silent -T {tmpDir}GD-{file}.mp3 https://nanao.teracloud.jp/dav/dir/GD-{file}.mp3 -u wec-test-1:WECWECWECWECWEC".format(tmpDir=tmpDir, file=file)
        os.system(cmd)
        remove.remove(file, "")

    except:
        sys.stderr.write(datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
        traceback.print_exc(file=sys.stderr)

# 複合関数 詳細は内容に併記
def getIPaddress(file):
    try:
        # ファイル変換
        exData(file)

        # hostlist 内のホスト名を1行ずつ読み取り、smartFileTransfer.sh に渡す
        # 転送処理の関数はthread.start()を利用。最後のスレッドはjoin()でロックさせる。（直後のファイル削除前に転送させるため）
        f = open("hostlist", 'r', encoding='utf-8')
        smartFT_thread = ""
        for cnt, list in enumerate(f):
            cnt = subprocess.getoutput("bash ./getIPaddress.sh {}".format(list))
            smartFT_thread = threading.Thread(target=smartFileTransfer, args=(file, cnt))
            smartFT_thread.start()
        smartFT_thread.join()
        
        f.close()
        print("transfer DONE.")

        # 転送が終わったらファイルを削除する
        remove.remove(file, "")
        print("remove DONE.")
    except:
        sys.stderr.write(datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
        traceback.print_exc(file=sys.stderr)

# ファイル名とIPアドレスを受け取り、sftpでデータ送信後、sshで再生を指示する。
def smartFileTransfer(file, ipaddress):
    try:
        print("START.{0}.{1}".format(file, ipaddress))
        command = "bash ./smartFileTransfer.sh {file} {ipaddress}".format(file=file, ipaddress=ipaddress)
        os.system(command)
        print("DONE.{0}.{1}".format(file, ipaddress))
    except:
        sys.stderr.write(datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
        traceback.print_exc(file=sys.stderr)


# 引数として、録音開始ボリュームのパラメータを受け取る。{arg}%
argvs = sys.argv  # コマンドライン引数を格納したリストの取得
argc = len(argvs) # 引数の個数

if (argc < 3):   # 引数の指定がない場合、start=0.2, end=2 を代入する
    argvs.append("0.2")
    argvs.append("2")

# 初回起動時に./file ディレクトリ内を削除する
try:
    remove.removeAll("")
except:
    pass

# メイン処理 time.sleep(3)は処理を中断させるための間
try:
    while True:
        rec = Recording(argvs[1], argvs[2])
        rec.record()
        upload_thread = threading.Thread(target=upload, args=(rec.date,))
        upload_thread.start()
        time.sleep(3)

except KeyboardInterrupt:
    print("stop")

except:
    sys.stderr.write(datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
    traceback.print_exc(file=sys.stderr)





