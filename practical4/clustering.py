# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:39:47 2018

@author: u2362
"""

#cluster

import sys
import re
from Bio.Blast import NCBIXML

genomes=[16,20,44,47]
refs=[]
seqs=[]
accs=[]
seq_accs=[]
for ref in genomes:
	for test in genomes:
		if ref!=test:		
			filehandle=open("./1_5_output/r"+str(ref)+"_"+str(test))
			for line in filehandle:
				ref_orf,seq,acc,seq_acc=line.split()
				refs.append(ref_orf)
				seqs.append(seq)
				accs.append(acc)
				seq_accs.append(seq_acc)

db={}
for one in range(len(refs)):
	if refs[one] not in db:
		db[refs[one]]=[refs[one],accs[one]]
	else:
		db[refs[one]].append(accs[one])
#print(db)
for element in db:		
	print(element,str(db[element]))
'''
for line in s:
	ref,seq,acc,seq_acc=line.split()
	print(acc)
'''
