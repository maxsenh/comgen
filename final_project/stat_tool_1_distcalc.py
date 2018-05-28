# -*- coding: utf-8 -*-
"""
Created on Thu May 24 14:39:52 2018

@author: u2362
"""

#1.1 Statistical tool - GC content and (di)nucleotide frequency

import sys

def gc_content(file_handle):
	op=open(file_handle)
	title=""
	seq=""
	for line in op:
		if line.startswith(">./"):
			title=line
		else:
			seq=line
	op.close()
	gc=(seq.count("C")+seq.count("G"))/len(seq)
	#print("genome: %s"%(title[3::]))
	print("GC-content: %.4f"%(gc))
	return gc,seq
	
	
#gc_content(sys.argv[1])
#nucl_freq(sys.argv[1])
#aminoacid_freq(sys.argv[1])

if __name__ == "__main__":
    gc_content('/genomes/16.fa.txt')