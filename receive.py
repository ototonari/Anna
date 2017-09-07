#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, time
from play import Player
from time import sleep
import sys, traceback

workTime = 18

now = datetime.now()
try:
    while now.hour < workTime:
        p = Player()
        p.checkFilelist()
        p.pickUpLog()
        p.extraction()
        p.importPlayedList()
        p.divide()
        p.sort()
        p.download()
        p.play()
        p.exportPlayedList()
        p.deleteLocal()
        sleep(30)
        now = datetime.now()

except:
    sys.stderr.write(datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
    traceback.print_exc(file=sys.stderr)
    pass

