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
	stop=["TGA","TAA","TAG"]
	orf_list=[]	
	for line in op:
		if line.startswith(">./"):
			title=line.strip()
		else:
			seq=line.strip()
	#5' - 3' 
	t2=0			
	for i in range(1,len(seq)-2):
		if seq[i-1:i+2] == "ATG" and i > t2: 					
			mid=[]
			for f in range(i-1,len(seq),3):		
				if seq[f:f+3] in stop:
					break					
				else:
					t2=f				
                 print(t2)
					if len(seq[f:f+3])==3:
						mid.append(seq[f:f+3])
			joined="".join(mid)
			if len(joined) > 1:
				orf_list.append(joined)
	#3' - 5' (rev)
	complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A','N':'N'}
	s=(''.join([complement[base] for base in seq[::-1]]))
	rev_list=[]
	t=0
	for i in range(1,len(s)-2):
		if s[i-1:i+2] == "ATG" and i > t:
			mid=[]
			for f in range(i-1,len(s),3):				
				if s[f:f+3] in stop:
					break					
				else:
					t=f
					if len(s[f:f+3])==3:
						mid.append(s[f:f+3])
			joined="".join(mid)
			if len(joined) > 1:
				rev_list.append(joined)
	print((orf_list))
	print(len(rev_list))
	print(len(seq))
	wr=open("out_orf"+str(file)[:2]+".fasta","w")
	for w in range(len(orf_list)):
		wr.write(">file_"+str(file)[:2]+"_orf_"+str(w)+"\n")
		wr.write(orf_list[w]+"\n")
	for w_rev in range(len(rev_list)):
		wr.write(">file_"+str(file)[:2]+"_orf_"+str(w_rev)+"_rev\n")
		wr.write(rev_list[w_rev]+"\n")
	wr.close()
orf_finder(sys.argv[1])
