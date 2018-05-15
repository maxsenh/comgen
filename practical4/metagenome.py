# -*- coding: utf-8 -*-
"""
Created on Mon May 14 17:51:14 2018

@author: u2362
"""

def parser(ins):
	seq16=[]
	seq20=[]
	seq44=[]
	seq47=[]
	for s in range(1):
		op=open(ins+str(s)).readlines()
		for line in range(len(op)):
			if op[line].startswith(">16"):
				for seq in range(line+1,len(op)):
					if op[seq].startswith(">"):
						break
					seq16.append(op[seq].strip("\n"))
			if op[line].startswith(">20"):
				for seq in range(line+1,len(op)):
					if op[seq].startswith(">"):
						break
					seq20.append(op[seq].strip("\n"))
			if op[line].startswith(">44"):
				for seq in range(line+1,len(op)):
					if op[seq].startswith(">"):
						break
					seq44.append(op[seq].strip("\n"))
			if op[line].startswith(">47"):
				for seq in range(line+1,len(op)):
					if op[seq].startswith(">"):
						break
					seq47.append(op[seq].strip("\n"))
	seq16complete="".join(seq16)
	seq20complete="".join(seq20)
	seq44complete="".join(seq44)
	seq47complete="".join(seq47)
	with open("metagenome","w") as writ:
		writ.write(">16\n%s\n>20\n%s\n>44\n%s\n>47\n%s\n"%(seq16complete,seq20complete,seq44complete,seq47complete))
	
	print(seq16)
parser("./kalign/koutFASTA_cluster")
