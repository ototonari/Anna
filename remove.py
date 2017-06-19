#!/usr/bin/env python
# -*- coding: utf-8 -*-

# DIR内の、引数の文字列に一致したファイルを削除する

import sys
import os
import re

def remove(filename):

    # target dir
    DIR = "./file/"
    
    fileList = os.listdir(DIR)
    pattern = re.compile(r'({})'.format(filename))

    for file in fileList:
        m = pattern.search(file)
        if m:
            os.remove("{dir}{file}".format(dir=DIR, file=m.string))

