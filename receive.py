#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, time
from play import Player
from time import sleep

now = datetime.now()
try:
    while now.hour <= 16:
        p = Player()
        p.checkFilelist()
        p.pickUpLog()
        p.extraction()
        p.sort()
        p.download()
        p.play()
        p.delete()
        sleep(60)
        now = datetime.now()

except:
    raise ValueError("play is Failure.")
