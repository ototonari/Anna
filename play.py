#!/usr/bin/env python
# -*- coding: utf-8 -*-

from check import playList
import os
import sys
from time import sleep

while True:
   f = open("playedList", 'a', encoding="utf-8")
   for file in playList():
      os.system("play {}".format(file)) # ファイル再生
      f.write("{},".format(file)) # 改行追加して記述
   f.close
   sleep(60)
   
