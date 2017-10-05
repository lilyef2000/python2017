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

#非数字
m = re.findall("\D", "abc1ab2c")
print m

#空白字符
m = re.findall("\s", "abc a\tb2c")
print m

#非空白字符
m = re.findall("\S", "abc a\tb2c")
print m

#数字和字母
m = re.findall("\w", "alan#123#--")
print m

#非数字和字母
m = re.findall("\W", "alan#123#--")
print m

#匹配开头
m = re.findall("^abc", "abcabc")
print m

#匹配结尾
m = re.findall("abc$", "abcabc")
print m

#不区分大小写
m = re.findall("abc", "abcdABc", re.I)
print m

#匹配换行
s = "<div>hello\nworld</div>"
m = re.findall(r"<div>(.*)</div>", s, re.S)
print m

#匹配多行
m = re.findall("^abc", "abc\nabc")
print m
m = re.findall("^abc", "abc\nabc", re.M)
print m

#匹配一个或0个
m = re.findall("ab?", "abbbbab")
print m

#匹配至少一个
m = re.findall("ab+", "abbbbabb")
print m

#匹配至少0个
m = re.findall("ab*", "aaabbb")
print m

#匹配出来org结尾的邮箱
m = re.findall("\w+@\w+\.org", "7636874@qq.com;763687@qq.org")
print m

#其他姿势
#如果是多次调用某个正则，则最好先编译后使用
p = re.compile("^abc")
m = p.findall("abc\nabc")
print m
m = p.findall("abcdef\nfdsfabc")
print m
m = p.findall("dabcdef\nefdsfabc")
print m

