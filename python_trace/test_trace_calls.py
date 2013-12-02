#!/usr/bin/python
import sys
from trace_calls import trace_calls

def b():
    print 'in b()'
    return

def a():
    print 'in a()'
    b()

class Class1:
    def method1(self):
        print 'method1'
sys.settrace(trace_calls)
a()
class1 = Class1()
class1.method1()
