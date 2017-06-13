#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import glob
import sys
import re
import os

# 説明しよう
# このスクリプトを実行すると、./file/ 内にあるファイル一覧から
# 一週間より古いデータを自動的に削除する。
# ちなみに判断基準はファイル名である。

# 一週間より古いかどうか判断する基準データの作成
now_time = datetime.now()
limit_time = now_time - timedelta(weeks=1)


# ./file/* ファイル一覧を取得する
fileList = glob.glob("./file/*")

# ファイル一覧を基準データと照らし合わせて、はみ出たデータを格納する
pattern = r"(([0-9]{4})-([0-9]{2})-([0-9]{2}))"

patternList = [n for n in fileList if re.search(pattern, n)]

removeList = []

for list in patternList:
    m = re.search(pattern, list)
    tmp_time = datetime.strptime(m.group(0), '%Y-%m-%d')
    chk_date = tmp_time - limit_time
    if 0 > chk_date.days:
        removeList.append(list)

f = open('remove.log', 'a')
for value in removeList:
    f.write("{}\n".format(value))
    os.remove(value)
f.close()




