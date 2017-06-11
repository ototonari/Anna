#!/bin/bash

#$1=FILE

FILE=$1

# .wav conversion .mp3 and gain
sox file/${FILE}.wav file/${FILE}.mp3
sox file/${FILE}.mp3 file/tmp${FILE}.mp3 gain -n
sox file/tmp${FILE}.mp3 file/GD-${FILE}.mp3 gain -l 5
