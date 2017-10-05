#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "--------输出从1加到100的结果--------"
total = 0
for i in range(1,101):
    total += i
print total

print "--------打印100以内质数--------"
def judge(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

for i in range(2,101):
    if judge(i):
        print i

print "--------计算一个文件中每个英文单词出现的次数--------"
f = open("test.txt")
lines = f.readlines()
f.close()
count = {}
for line in lines:
    tokens = line.strip().split(' ')
    for token in tokens:
        if token not in count:
            count[token] = 0
        count[token] += 1

for word in count:
    print word,count[word]
