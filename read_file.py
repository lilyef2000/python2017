#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
f = open("test.txt")
content = f.read()
f.close() # 一定要close掉

print content
'''

f = open("test.txt")
while True:
    lines = f.readlines(10000)
    if not lines:
	    break
    for line in lines:
	    print line.strip()
		
		
		
f = open("test.txt","a")
f.writelines(["hhhhhh","llllll"])
f.close