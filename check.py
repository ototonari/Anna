#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, time
import glob
import sys
import re
import os

# このスクリプトはクラウドディレクトリを確認し、未再生のファイルを順次再生する。
# 判断基準として、テキストファイルで再生済みのデータを書き出し、候補に入れないようにしている。
# また、絞り込みとして、ファイル名が基準に満たしているかどうか、当日のデータであるか、再生していないかどうかで判断する。
# ちなみに判断基準はファイル名である。

def playList():
    # ./file/* ファイル一覧を取得する
    fileList = glob.glob("./share/*")


    # 絞り込み　ファイル名が基準通りか
    pattern = r"(([0-9]{4})-([0-9]{2})-([0-9]{2}))"
    patternList = [n for n in fileList if re.search(pattern, n)]


    # 絞り込み　当日のデータかどうか
    todayList = []  # 本日の日付のデータパスを格納する
    now_time = datetime.now() # - timedelta(days=3) # 日付補正

    for list in patternList:
        m = re.search(pattern, list)
        tmp_time = datetime.strptime(m.group(0), '%Y-%m-%d')
        # 今日の日付と等しいかどうか評価する
        if ((tmp_time.year == now_time.year) and (tmp_time.month == now_time.month) and (tmp_time.day == now_time.day)):
            todayList.append(list)    


    # 分岐　再生済みデータがあれば、差分を返す。無ければそのまま返す。
    pattern = r"[0-9]{2}:[0-9]{2}:[0-9]{2}"
    # 並び替え　再生ファイルを古い順に並び替える
    sortedTodayList = sorted(todayList, key=lambda x: datetime.strptime(re.search(pattern, x).group(0), '%H:%M:%S'))

    # 確認　再生済みデータ
    if os.path.isfile("./playedList"):
        # 再生済みデータをSET型に格納
        played = set()
        f = open("playedList", 'r', encoding="utf-8")
        s = f.read()
        played = {line for line in s.split(",") if (line != "")}
        
        # 未再生のデータを抽出
        newPlayList = []
        #newPlayList = [line for line in sortedTodayList if set(line) not in played]
        if set(sortedTodayList[0]) in played:
            print("True")
        #return newPlayList    
    else:
        return sortedTodayList

