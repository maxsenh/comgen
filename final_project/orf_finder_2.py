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
	for j in range(3):
		t=0	
		for i in range(j,len(seq)-1,3):
			if seq[i-1:i+2] == "ATG" and i > t: 					
				mid=[]
				for f in range(i-1,len(seq),3):		
					if seq[f:f+3] in stop:
						break					
					else:
						t=f				
					if len(seq[f:f+3])==3:
						mid.append(seq[f:f+3])
				joined="".join(mid)
				if len(joined) > 100 and len(joined) < 1500:
					orf_list.append(joined)
					
	#3' - 5' (rev)
	complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A','N':'N'}
	s=(''.join([complement[base] for base in seq[::-1]]))
	rev_list=[]
	for j2 in range(3):
		t2=0		
		for i2 in range(j2,len(s)-1,3):
			if s[i2-1:i2+2] == "ATG" and i2 > t2:
				mid=[]
				for f2 in range(i2-1,len(s),3):				
					if s[f2:f2+3] in stop:
						break					
					else:
						t2=f2
						if len(s[f2:f2+3])==3:
							mid.append(s[f2:f2+3])
				joined="".join(mid)
				if len(joined) > 100 and len(joined) < 1500:
					rev_list.append(joined)
	print(len(orf_list))
	print(len(rev_list))
	print(len(seq))
	print(s.count("ATG"))
	print(seq.count("ATG"))
	
	wr=open("out_orf"+str(file)[:2]+".fasta","w")
	for w in range(len(orf_list)):
		wr.write(">file_"+str(file)[:2]+"_orf_"+str(w)+"\n")
		wr.write(orf_list[w]+"\n")
	for w_rev in range(len(rev_list)):
		wr.write(">file_"+str(file)[:2]+"_orf_"+str(w_rev)+"_rev\n")
		wr.write(rev_list[w_rev]+"\n")
	wr.close()
orf_finder(sys.argv[1])
