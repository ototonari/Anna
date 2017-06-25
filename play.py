#!/usr/bin/env python
# -*- coding: utf-8 -*-

from check import playList
import os
import sys

f = open("playedList", 'a', encoding="utf-8")
for file in playList():
   print(file) # 再生したとみなす
   f.write("{},".format(file)) # 改行追加して記述
f.close
