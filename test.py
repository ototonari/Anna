#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys
from time import sleep
from datetime import datetime, timedelta, time


class Player():
    def __init__(self):
        self.playList = []
        self.fileList = []
        self.playedList = []
        self.pattern = re.compile('GD.+mp3')
        self.logFile = ""
        self.url = "https://nanao.teracloud.jp/dav/dir/"
        self.user = "wec-test-1"
        self.password = "WECWECWECWECWEC"
        self.auth = "-u {u}:{p}".format(u=self.user, p=self.password)
        self.log = "./log"
        self.cmd_getList = "curl -X PROPFIND {auth} '{url}' -o {log}".format(auth=self.auth, url=self.url, log=self.log)
        

    def checkFilelist(self):
        try:
            os.system(self.cmd_getList)
        except:
            raise ValueError("checkFilelist is Failure.")

    def pickUpLog(self):
        with open(self.log, 'r') as file:
            self.logFile = file.read()

    def extraction(self):
        if self.logFile:
            for file in self.pattern.finditer(self.logFile):
                self.fileList.append(file.group())

    def sort(self):
        if self.logFile:
            pattern = r"[0-9]{2}:[0-9]{2}:[0-9]{2}"
            sortedList = sorted(self.fileList, key=lambda x: datetime.strptime(re.search(pattern, x).group(0), '%H:%M:%S'))
            self.playList = sortedList
    
    def divide(self):
        try:
            if self.fileList:
                self.playList = [line for line in self.fileList if line not in self.playedSet]
        except:
            pass

    def download(self):
        try:
            for file in self.playList:
                cmd_getFile = "curl -O {url}{file} {auth} -o ./download/{file}".format(url=self.url, file=file, auth=self.auth)
                os.system(cmd_getFile)
        except:
            raise ValueError("download is Failure.")

    def play(self):
        try:
            for file in self.playList:
                os.system("play {}".format(file))
                self.playedList.append(file)
        except:
            raise ValueError("play is Failure.")

    def delete(self):
        try:
            pass
        except:
            raise ValueError("delete is Failure.")