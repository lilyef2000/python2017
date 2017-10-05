#_*_ coding:utf-8 _*_

print u"--------函数赋值给变量--------"
def func_add(x, y):
    return x + y
f = func_add
print id(f)
print id(func_add)

print u"--------高阶函数--------"
def func_add(x, y):
    return x + y

def func_high(func, x, y):
    return func(x, y)
print func_high(func_add, 1, 2)

print u"--------匿名函数--------"
add = lambda x,y: x + y
print add(1, 2)

print u"--------闭包--------"
def closure(x):
    def func_double():
        return x*2
    return func_double
c = closure(1)
print c
print c()