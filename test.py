#!/usr/bin/python
import os,sys

if len(sys.argv)==1:
    filename='test.c'
else:
    filename=sys.argv[1]

def printResult(op):
    for line in op.readlines():print(line)

reward = os.popen('gcc %s -o %s' % (os.getcwd()+os.sep+filename,os.getcwd()+os.sep+filename[0:-2]))
printResult(reward)

result = os.popen('%s' % os.getcwd()+os.sep+filename[0:-2])
printResult(result)

os.system('rm %s' % os.getcwd()+os.sep+filename[0:-2])
