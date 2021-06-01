#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time 

count=0
while(True):
    count = count+1
    print("Hello count = "+str(count))
    time.sleep(1)
    if(count > 60):
        break
