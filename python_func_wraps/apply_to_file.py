#!/usr/bin/python
#encoding=utf-8
import sys
if len(sys.argv) != 2 and len(sys.argv) != 3:
    print 'Usage: <infile> [outfile]'
    sys.exit(0)

imported = False
outbuf = ''
infile = open(sys.argv[1])
while True:
    #读取一行
    line = infile.readline()
    if not line:
        break
    line = line.strip('\r\n')

    #计算缩进
    indent = ''
    pos = 0
    while pos < len(line) and (line[pos] == ' ' or line[pos] == '\t'):
        pos += 1
    if pos > 0:
        indent = line[0:pos]
    statement = line[pos:]

    #import库
    if not imported:
        if not statement.startswith('#'):
            outbuf += indent + 'from TraceCalls import TraceCalls\n'
            imported = True

    #输出wrap
    if statement.startswith('def '):
        outbuf += indent + '@TraceCalls()\n'

    #输出一行
    outbuf += indent + statement + '\n'
infile.close()

outfile = open(len(sys.argv) == 2 and sys.argv[1] or sys.argv[2], 'w')
outfile.write(outbuf)
outfile.close()
