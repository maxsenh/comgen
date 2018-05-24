# -*- coding: utf-8 -*-
"""
Created on Thu May 24 15:20:07 2018

@author: u2362
"""
import sys

#2. ORF-finder

def orf_finder(file):
	op=open("./genomes/"+file)
	title=""
	seq=""
	for line in op:
		if line.startswith(">./"):
			title=line
		else:
			seq=line
	for i in range(1,len(seq)-2):
		if seq[i-1:i+2] == "ATG":
			
	
orf_finder(sys.argv[1])