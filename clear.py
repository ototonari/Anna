#!/usr/bin/env python
# -*- coding: utf-8 -*-

# main 引数に応じて処理する。
#     local  = ダウンロードデータの削除、再生済みリストの削除
#     global = local に加えて、クラウド上のデータを削除する

from play import Player
from datetime import datetime
import sys, traceback

    # main
try:
    if __name__ == '__main__':
        args = sys.argv
        if len(args) > 1:
            # switch
            p = Player()
            if args[1] == 'local':
                p.deleteLocal()
            elif args[1] == 'remote':
                p.deleteRemote()
            else:
                raise ValueError("引数が正しくありません")

except:
    sys.stderr.write(datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n"))
    traceback.print_exc(file=sys.stderr)
