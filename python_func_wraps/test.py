#!/usr/bin/python

def iseven(n):
    return True if n == 0 else isodd(n - 1)

def isodd(n):
    return False if n == 0 else iseven(n - 1)

print(iseven(7))
