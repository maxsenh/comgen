# -*- coding: utf-8 -*-
"""
Created on Thu May 17 14:41:03 2018

@author: u2362
"""

import sys, re

def parse(inputfile,outputfile):
	ind=open(inputfile)
	out=open(outputfile,"w")
	nr2=[]
	seq2=[]
	for line in ind:
		x,y=line.split()
		out.write(y)
	ind.close()
	out.close()
	
parse(sys.argv[1],sys.argv[2])