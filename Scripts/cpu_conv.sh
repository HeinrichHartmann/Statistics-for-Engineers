#!/bin/bash

cat | perl -pe 's/^ *| *$//g' | perl -pe 's/ +/,/g'
