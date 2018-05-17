#! /usr/bin/env python
"prints first argument aa sequences of length second argument to screen"
import random
import sys

number=int(sys.argv[1])
length=int(sys.argv[2])
aas="ARNDCEQGHILKMFPSTWYV"
def r20():
    return random.randrange(20)
db={}
op=open("randomseq"+str(input())+".txt","w")
for i in range(number):
    s=""
    for j in range(length):
        s+=aas[r20()]
    print (s)
    db[i]=s
    op.write("%s      %s"%(i,s))
op.close()