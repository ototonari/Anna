#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys, traceback
from time import sleep
from datetime import datetime, timedelta, time
import remove
import subprocess, shlex
import pickle


class Player():
    def __init__(self):
        self.playList = []
        self.fileList = []
        self.playedSet = set()
        self.playedList = []
        self.pattern = re.compile('GD.+mp3')
        self.pickle = "./play.playedList"
        self.localDir = "./download/"
        self.logFile = ""
        self.url = "https://nanao.teracloud.jp/dav/dir/"
        self.user = "wec-test-1"
        self.password = "WECWECWECWECWEC"
        self.auth = "-u {u}:{p}".format(u=self.user, p=self.password)
        self.log = "./log"
        self.cmd_getList = "curl --silent -X PROPFIND {auth} '{url}' -o {log}".format(auth=self.auth, url=self.url, log=self.log)
        
    # teraCloudのファイルの一覧を取得し ./log に出力
    def checkFilelist(self):
        try:
            print("start checkFilelist")
            #os.system(self.cmd_getList)
            args = shlex.split(self.cmd_getList)
            p = subprocess.run(args)
            sleep(5)
        except:
            sys.stderr.write(datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
            traceback.print_exc(file=sys.stderr)

    # ./log ファイルを読み込みオブジェクトに格納する
    def pickUpLog(self):
        with open(self.log, 'r') as file:
            self.logFile = file.read()

    # 格納されたファイル一覧を配列として再格納する
    def extraction(self):
        if self.logFile:
            for file in self.pattern.finditer(self.logFile):
                self.fileList.append(file.group())
    
    # pickle化された外部データを読み込みオブジェクトに取り込む
    def importPlayedList(self):
        try:
            if os.path.exists(self.pickle):
                with open(self.pickle, 'rb') as f:
                    tmpFile = pickle.load(f)
                    self.playedSet = {file for file in tmpFile if file}
                    self.playedList = tmpFile

        except:
            sys.stderr.write(datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
            traceback.print_exc(file=sys.stderr)

    # 再生済みのデータを除いて、プレイリストを作成する
    def divide(self):
        try:
            if self.fileList:
                self.playList = [file for file in self.fileList if file not in self.playedSet]
        except:
            sys.stderr.write(datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
            traceback.print_exc(file=sys.stderr)

    # ファイル一覧を日時でソートする
    def oldSort(self):
        try:
            if self.fileList:
                pattern = r"[0-9]{2}:[0-9]{2}:[0-9]{2}"
                sortedList = sorted(self.fileList, key=lambda x: datetime.strptime(re.search(pattern, x).group(0), '%H:%M:%S'))
                self.fileList = sortedList
        except:
            sys.stderr.write(datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
            traceback.print_exc(file=sys.stderr)

    def sort(self):
        try:
            if self.playList:
                tmpList = self.playList
                self.playList = sorted(tmpList)

        except:
            sys.stderr.write(datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
            traceback.print_exc(file=sys.stderr)

    # ファイル一覧を読み込み、teraCloudからダウンロードする
    def download(self):
        try:
            if os.path.exists(self.localDir) == False:
                print("make dir ./download")
                os.makedirs(self.localDir)

            if self.playList:
                for file in self.playList:
                    cmd_getFile = "curl -o {ldir}{file} {url}{file} {auth}".format(ldir=self.localDir, url=self.url, file=file, auth=self.auth)
                    os.system(cmd_getFile)
        except:
            sys.stderr.write(datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
            traceback.print_exc(file=sys.stderr)

    # ファイル一覧からファイル名を順に読み込み、再生する。また再生したファイル名は再生済みリストに追加する。
    def play(self):
        try:
            if self.playList:
                for file in self.playList:
                    cmd_playFile = "play {ldir}{file}".format(ldir=self.localDir, file=file)
                    os.system(cmd_playFile)
                    self.playedList.append(file)
                    sleep(1)
        except:
            sys.stderr.write(datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
            traceback.print_exc(file=sys.stderr)

    # 再生済みリストを外部ファイルに書き出す。(pickle化して出力)
    def exportPlayedList(self):
        try:
            if self.playedList:
                with open(self.pickle, 'wb') as f:
                    pickle.dump(self.playedList, f)

        except:
            sys.stderr.write(datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
            traceback.print_exc(file=sys.stderr)


    # receive.py 用メソッド
    # 再生済みリストを読み込み、その音声データがローカルに存在していた場合は削除する
    def delete(self):
        try:
            if self.playedList:
                for file in self.playedList:
                    if os.path.exists("{dir}{file}".format(dir=self.localDir, file=file)):
                        remove.remove(file, self.localDir)

        except:
            sys.stderr.write(datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
            traceback.print_exc(file=sys.stderr)


    # manager.py 用メソッド
    # ローカルのpickleファイルとダウンロードデータを削除する
    def deleteLocal(self):
        try:
            self.importPlayedList()
            self.delete()
            if os.path.exists(self.pickle):
                os.remove(self.pickle)

        except:
            sys.stderr.write(datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
            traceback.print_exc(file=sys.stderr)


    # manager.py 用メソッド
    # 注意！！このメソッドを呼び出した場合、play.playedListを削除します。
    # またteraCloud内のデータもplayedListに含まれる分を削除するため、初期化する際のみ呼び出してください。
    # メインループに組み込まないでください！！！！！
    def deleteRemote(self):
        try:
            self.importPlayedList()
            if self.playedList:
                for file in self.playedList:
                    cmd_deleteFile = "curl -X DELETE {url}{file} {auth}".format(url=self.url, file=file, auth=self.auth)
                    os.system(cmd_deleteFile)
            if os.path.exists(self.pickle):
                os.remove(self.pickle)

        except:
            sys.stderr.write(datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
            traceback.print_exc(file=sys.stderr)

    # 渡された引数に応じて、関数を呼び出す
    def checkArgs(self):
        try:
            params = sys.argv
            if params > 1:
                # 引数に応じて処理する

                # params[1] == delete ならクラウドストレージから再生済みのデータを削除する
                if params[1] == 'delete':
                    self.deleteRemote()
            
    
            
        except:
            sys.stderr.write(datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
            traceback.print_exc(file=sys.stderr)
