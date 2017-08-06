#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess, sys, shlex


def checkProcessId(script, file):
    awk = "awk '$(NF-1) ~ /^%s$/ && $NF ~ /^%s$/ {print $2}'" % (script, file)
    cmd = "ps aux | {awk}".format(awk=awk)
    result = subprocess.getoutput(cmd)
    if result:
        return result
    else:
        return 0

def generateProcess(script, file):
    cmd = "{} {}".format(script, file)
    args = shlex.split(cmd)
    p = subprocess.Popen(args)

def killProcess(processId):
    cmd = "kill {}".format(processId)
    args = shlex.split(cmd)
    p = subprocess.Popen(args)

def shellCommand(commands):
    args = shlex.split(commands)
    result = subprocess.getoutput(args)
    return result

