#!/usr/bin/python
# -*- coding: UTF-8 -*-

str = 'Hello World!'

print str # 输出完整字符串
print str[0] # 输出字符串中的第一个字符
print str[2:5] # 输出字符串中第三个至第五个之间的字符串
print str[2:] # 输出从第三个字符开始的字符串
print str * 2 # 输出字符串两次
print str + "TEST" # 输出连接的字符串

list_a = ["str", 1, ["a", "b", "c"], 4]
list_b = ["hello"]
print list_a[0]
print list_a[1:3]
print list_a[1:]
print list_b * 2
print list_a + list_b

tuple_a = ("str", 1, ["a", "b", "c"], 4)
tuple_b = ("hello",)
print tuple_a[0]
print tuple_a[1:3]
print tuple_a[1:]
print tuple_b * 2
print tuple_a + tuple_b

dict_a = {
"name": "Alan",
"age": 24,
1: "level_1"
}

print dict_a["name"]
print dict_a["age"]
print dict_a[1]

print "name" in dict_a
print "xxx" in dict_a
print dict_a.keys()
print dict_a.values()
print dict_a.items()
