#!/bin/bash
# -*- coding: utf-8 -*-

#$1=FILE

FILE=$1

# .wav conversion .mp3 and gain  and remove
sox file/${FILE}.wav file/${FILE}.mp3
rm file/${FILE}.wav
sox file/${FILE}.mp3 file/tmp${FILE}.mp3 gain -n
rm file/${FILE}.mp3
sox file/tmp${FILE}.mp3 file/GD-${FILE}.mp3 gain -l 5
rm file/tmp${FILE}.mp3

