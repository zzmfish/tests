#!/usr/bin/python
#encoding=utf-8
#no-apply-func-wrap
import sys
import os.path
from functools import wraps

stream = open('trace.log', 'w')

class TraceCalls(object):
    """ Use as a decorator on functions that should be traced. Several
        functions can be decorated - they will all be indented according
        to their call depth.
    """
    def __init__(self, indent_step=2, show_ret=False):
        self.indent_step = indent_step
        self.show_ret = show_ret

        # This is a class attribute since we want to share the indentation
        # level between different traced functions, in case they call
        # each other.
        TraceCalls.cur_indent = 0

    def __call__(self, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            func_name = fn.__name__
            if func_name == '__repr__':
                return #避免递归
            indent = ' ' * TraceCalls.cur_indent
            argstr =  '' #', '.join(
                #[repr(a) for a in args] +
                #["%s=%s" % (a, repr(b)) for a, b in kwargs.items()])
            file_name = os.path.basename(fn.func_code.co_filename)
            line_num = fn.func_code.co_firstlineno
            stream.write('%20s:%5d: %s%s(%s)\n' % (file_name, line_num, indent, func_name, argstr))

            TraceCalls.cur_indent += self.indent_step
            ret = fn(*args, **kwargs)
            TraceCalls.cur_indent -= self.indent_step

            if self.show_ret:
                stream.write('%s--> %s\n' % (indent, ret))
            return ret
        return wrapper
