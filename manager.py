#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess, sys, shlex, traceback, datetime

def checkProcessId(script, file):
    awk = "awk '$11 ~ /^%s$/ && $12 ~ /^%s$/ {print $2}'" % (script, file)
    cmd = "ps aux | {awk}".format(awk=awk)
    result = subprocess.getoutput(cmd)
    if result:
        print("process is exist.")
        return result
    else:
        print("process is nothing.")
        return 0

def generateProcess(args):
    try:
        if args:
            cmd = ""
            for line in args:
                cmd += "{} ".format(line)
            args = shlex.split(cmd)
            p = subprocess.Popen(args)
            print("generateProcess to {cmd}".format(cmd=cmd))
        else:
            print("don't generateProcess. no argument.")

    except:
        sys.stderr.write(datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
        traceback.print_exc(file=sys.stderr)


def killProcess(processId):
    cmd = "kill {}".format(processId)
    args = shlex.split(cmd)
    p = subprocess.Popen(args)
    print("killProcess to pid {pid}".format(pid=processId))

def familyKilling(parentName):
    cmd = "bash ./killpstree.bash {}".format(parentName)
    args = shlex.split(cmd)
    p = subprocess.Popen(args)
    print("Killing {}'s family".format(parentName))

def shellCommand(commands):
    args = shlex.split(commands)
    result = subprocess.getoutput(args)
    return result



try:
    if __name__ == '__main__':
        argvs = sys.argv
        order = argvs[1]
        args = argvs[2:]
        if order == "generate":
            if checkProcessId(args[0], args[1]) == 0:
                generateProcess(args)

        elif order == "kill":
            processId = checkProcessId(args[0], args[1])
            if processId:
                killProcess(processId)

        elif order == "killing":
            if args[1]:
                familyKilling(args[1])

except IndexError:
    print(sys.exc_info()[0])
    print("usage: manager.py - generate or kill or killing - scriptname - filename")
    print("exp) python manager.py generate python record.py")
    sys.stderr.write(datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
    traceback.print_exc(file=sys.stderr)
except:
    sys.stderr.write(datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
    traceback.print_exc(file=sys.stderr)