#!/bin/python

import sys
from collections import Counter


Q = int(raw_input().strip())
for a0 in xrange(Q):
    n = int(raw_input().strip())
    b = raw_input().strip()
    
    dic = Counter(b)
    if (len(dic.keys()) > (n/2)) or (dic['_'] <1):
        print "NO"
    else:
        keys = dic.keys()
        flag = True
        if '_' in keys:
            keys.remove('_')
            for color in keys:
                if dic[color] < 2:
                    flag = False
        else:
            colors = iter(n)
            prev_color = next(colors)
            for cur_color in colors:
                if prev_color == cur_color:
                    if flag:
                        flag = True
                    else:
                        flag = False
        if flag:
            print "YES"
        else:
            print "NO"



