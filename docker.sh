#!/bin/bash

cd `dirname $0`

docker run --rm -it "$@" \
       -p 9990-9999:9990-9999 \
       -v $(pwd):/home/jovyan/work \
       -v $HOME:/home/jovyan/host/home \
       -v /:/home/jovyan/host/root \
       heinrichhartmann/jupyter
