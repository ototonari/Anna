#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 一日の始まりに実行する
import os

# playedList　を削除する
if os.path.isfile("./playedList"):
    os.remove("./playedList")

# one_week.py を実行する
os.system("python ./one_week.py")