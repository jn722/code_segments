#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 打开一个文件

import re
import sys

dictMcast = {}


try:
    fo = open("jack.log", "r")
    while True:
        line = fo.readline()
        if line == "":
            break
        # print(line)
        matchObj = re.match( r'JackMcastForwarder\:\:AddJackMcastSession\: mac= (.+) vid=', line)
 
        if matchObj:
            # print ("matchObj.group(1) : ", matchObj.group(1))
            key = matchObj.group(1)
            print("add", key)
            if dictMcast.get(key) == None:
                dictMcast[key] = 1
            else:
                dictMcast[key] += 1
                print(key, dictMcast[key])
                sys.exit(1)

        
        matchObj = re.match( r'JackMcastForwarder\:\:DelJackMcastSession\: mac=(.+) vid=', line)
        if matchObj:
            # print ("matchObj.group(1) : ", matchObj.group(1))
            key = matchObj.group(1)
            if dictMcast.get(key) != None:
                dictMcast[key] -= 1
                # print("del", key)
                if dictMcast[key] == 0:
                    print("del", key)
                    del dictMcast[key]


    print("共有不同的组播地址：",len(dictMcast.keys()))
    for key in dictMcast.keys():
        print(key, dictMcast[key])

except Exception as e:
    print(e)
finally:
    # 关闭打开的文件
    # print("aaa")
    fo.close()
