#!/usr/bin/env python
# encoding: utf-8

indent = ''

def trace_calls(frame, event, arg):
    if event != 'call' and event != 'return':
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    line_no = frame.f_lineno
    file_name = co.co_filename
    print 'trace# \x1b[33m%s\x1b[0m    @%s:%d' % (func_name, file_name, line_no)
    return


