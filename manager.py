#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess, sys, shlex, traceback

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
        print(sys.exc_info()[0])
        traceback.print_exc(file=sys.stdout)
        pass


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
    print("python manager.py order script filename")
except:
    print(sys.exc_info()[0])
    traceback.print_exc(file=sys.stdout)
    pass
