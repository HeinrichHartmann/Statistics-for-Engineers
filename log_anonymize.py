#!/usr/bin/python

import sys
import re

urls = {}
cnt = 0

for l in sys.stdin:
    method, url, prot = re.findall('"(.*?) (.*?) (HTTP/1.1)"', l)[0]

    if not url in urls:
        urls[url] = cnt
        cnt += 1
    rep = "/doc/" + str(urls[url])
    
    
    sys.stdout.write(
        re.sub('"(.*?) (.*?) (.*?)"', '"{} {} {}"'.format(method, rep, prot), l)
    )