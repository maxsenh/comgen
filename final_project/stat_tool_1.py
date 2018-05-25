# -*- coding: utf-8 -*-
"""
Created on Thu May 24 14:39:52 2018

@author: u2362
"""

#1.1 Statistical tool - GC content and (di)nucleotide frequency

import sys

def gc_content(file):
	op=open("./genomes/"+file)
	title=""
	seq=""
	for line in op:
		if line.startswith(">./"):
			title=line
		else:
			seq=line
	op.close()
	gc=(seq.count("C")+seq.count("G"))/len(seq)
	print("genome: %s"%(title[3::]))
	#print("GC-content: %.4f"%(gc))
	return gc,seq
	
def nucl_freq(file):
	gc,seq=gc_content(file)
	sett=["A","C","G","T","N","AA","AC","AT","AG","CA","CC","CT","CG","TA","TC","TT","TG","GA","GC","GT","GG"]
	print("GC-content: %.4f"%(gc))
	for nucl in sett:		
		print("#%s = %d/%d"%(nucl,seq.count("A"),len(seq)))
	'''
	print("#C = %d/%d"%(seq.count("C"),len(seq)))
	print("#T = %d/%d"%(seq.count("T"),len(seq)))
	print("#G = %d/%d"%(seq.count("G"),len(seq)))
	print("#N = %d/%d"%(seq.count("N"),len(seq)))

	print("#AA = %d/%d"%(seq.count("AA"),len(seq)))
	print("#AC = %d/%d"%(seq.count("AC"),len(seq)))
	print("#AT = %d/%d"%(seq.count("AT"),len(seq)))
	print("#AG = %d/%d"%(seq.count("AG"),len(seq)))
	
	print("#CA = %d/%d"%(seq.count("CA"),len(seq)))
	print("#CC = %d/%d"%(seq.count("CC"),len(seq)))
	print("#CT = %d/%d"%(seq.count("CT"),len(seq)))
	print("#CG = %d/%d"%(seq.count("CG"),len(seq)))
	
	print("#TA = %d/%d"%(seq.count("TA"),len(seq)))
	print("#TC = %d/%d"%(seq.count("TC"),len(seq)))
	print("#TT = %d/%d"%(seq.count("TT"),len(seq)))
	print("#TG = %d/%d"%(seq.count("TG"),len(seq)))
	
	print("#GA = %d/%d"%(seq.count("GA"),len(seq)))
	print("#GC = %d/%d"%(seq.count("GC"),len(seq)))
	print("#GT = %d/%d"%(seq.count("GT"),len(seq)))
	print("#GG = %d/%d"%(seq.count("GG"),len(seq)))
	'''
def aminoacid_freq(file):
	op=open("./proteomes/"+file)
	sett="ACDEFGHIKLMNPQRSTVWY"
	seq=[]
	for line in op:
		if line.startswith(">./")==False:
			seq.append(line.strip())
	seq="".join(seq)
	op.close()
	print("Amino acid frequency:\n")
	for amino in sett:
		print("#%s = %d/%d"%(amino,seq.count(str(amino)),len(seq)))
	
#gc_content(sys.argv[1])
nucl_freq(sys.argv[1])
#aminoacid_freq(sys.argv[1])