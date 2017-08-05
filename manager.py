#!/usr/bin/env python
# -*- coding: utf-8 -*-

# crontab によって５分置きに実行される
# 録音端末の場合 record.py が起動されているか確認し終了していた場合は起動させる
# 再生端末の場合 receive.py が起動されているか確認し終了していた場合は起動させる

import subprocess, sys, shlex


def checkProcessId(script, file):
    awk = "awk '$(NF-1) ~ /^%s$/ && $NF ~ /^%s$/ {print $2}'" % (script, file)
    cmd = "ps aux | {awk}".format(awk=awk)
    result = subprocess.getoutput(cmd)
    if result:
        return result
    else:
        return 0

def generateProcess():
    cmd = "python record.py"
    args = shlex.split(cmd)
    p = subprocess.Popen(args)

argvs = sys.argv
if (len(argvs) < 2):
    argvs.append("python")
    argvs.append("record.py")

if checkProcessId(argvs[1], argvs[2]):
    generateProcess()

