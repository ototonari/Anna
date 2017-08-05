#!/usr/bin/env python
# -*- coding: utf-8 -*-

# crontab によって５分置きに実行される
# 録音端末の場合 record.py が起動されているか確認し終了していた場合は起動させる
# 再生端末の場合 receive.py が起動されているか確認し終了していた場合は起動させる

import os
import sys
import subprocess
from datetime import datetime, timedelta, time

class ProcessManager():
    def __init__(self):
        

if __name__ == '__main__':
    cmd = 'ps aux | grep record.py'
    result = subprocess.getoutput(cmd)
    print(result)
