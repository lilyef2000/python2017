#-*- coding: UTF-8 -*-

import sys
type = sys.getfilesystemencoding()

import urllib2
import re
response = urllib2.urlopen('http://blog.leanote.com/qq-alan')
html = response.read()
#print html
#m = re.findall(r'title="全文">(.*?)</a>', html)
#m = re.findall(r'title="全文">(.*)</a>', html, re.S)
#m = re.findall(r'title="全文">(.*?)</a>', html)
m = re.findall(r'<div class="title">.*?title="全文">(.*?)</a>', html, re.S)
for t in m:
    print t.decode('utf-8').encode(type)