#_*_ coding:utf-8 _*_

import re

#匹配除了换行符之外的所有字符
m = re.findall(".","aa\nbbcc")
print m

#转义字符
m = re.findall("\.", "a.c")
print m

#字符集
m = re.findall("a[bcd]e","abeaceade")
print m

#数字
m = re.findall("\d","abc1ab2c")
print m