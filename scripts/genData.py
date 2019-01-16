#!/usr/bin/python
import random
import sys

f = open('graph'+sys.argv[1]+'_'+sys.argv[2]+'.txt','w')

maxN = int(sys.argv[1])
step = int(maxN/int(sys.argv[2]))
for i in range(maxN):
    curN = 0
    curN += random.randint(0,step)
    while curN <= maxN:
        if curN != i:
            newline = "site"+ str(i)+" site"+str(curN)+"\n"
            f.write(newline)
        curN += random.randint(0,step)
