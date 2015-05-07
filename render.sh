#!/bin/bash

PID=`cat slides.pid`

echo "Killing process $PID"
kill $PID

~/Programs/anaconda/bin/ipython nbconvert Tutorial.ipynb --to slides --post serve &

echo $! > slides.pid
