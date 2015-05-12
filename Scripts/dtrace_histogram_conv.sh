#!/bin/bash
cat |\
tail -n +2 |\
perl -pe 's/^\D*(\d+)\D*(\d+)\D*\n$/\1,\2\n/'
