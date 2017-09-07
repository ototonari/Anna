#!/usr/bin/env python
# -*- coding: utf-8 -*-

# DIR内の、引数の文字列に一致したファイルを削除する

import sys, os, re, traceback
from time import sleep
from datetime import datetime, timedelta, time
from play import Player
import subprocess, shlex
import pickle


def remove(filename, directory):

    # target dir
    DIR = directory or "./file/"
    
    fileList = os.listdir(DIR)
    pattern = re.compile(r'({})'.format(filename))

    for file in fileList:
        m = pattern.search(file)
        if m:
            os.remove("{dir}{file}".format(dir=DIR, file=m.string))

def removeAll(directory):
    directory = directory or "./file/"
    fileList = os.listdir(directory)
    for file in fileList:
        os.remove("{dir}{file}".format(dir=directory, file=file))


    # main
try:
    if __name__ == '__main__':
        p = Player()
        p.checkArgs

except:
    sys.stderr.write(datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
    traceback.print_exc(file=sys.stderr)
