#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Annaシステムの各プロセスのタイムスケジューラーファイル
# 主にlinux立ち上げ時に一緒に起動されることを想定している

from time import sleep
import os
import sys
from datetime import datetime, timedelta, date

def checkTime():
    

