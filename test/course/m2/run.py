#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
import hello
hello.print_hello()


# python的模块
import sys
sys.path.append('./test')
import hello
hello.print_hello()
'''
# python的包
import os
import sys
sys.path.append('../../../test')
from course.m1 import b
from course.m1.m1_1 import a

if __name__ == '__main__':
   b.hello_b()
   a.hello_a()