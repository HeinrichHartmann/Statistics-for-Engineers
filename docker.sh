#!/bin/bash

cd `dirname $0`

podman run --rm -it "$@" \
       -p 9990-9999:9990-9999 \
       -v $(pwd):/home/jovyan/work \
       heinrichhartmann/jupyter
