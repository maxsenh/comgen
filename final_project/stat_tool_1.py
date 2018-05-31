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
	#print("genome: %s"%(title[3::]))
	#print("GC-content: %.4f"%(gc))
	return gc,seq
	
def nucl_freq(file):
    gc,seq=gc_content(file)
    sett=["A","C","G","T","N"]
    sett_duo=["AA","AC","AT","AG","CA","CC","CT","CG","TA","TC","TT","TG","GA","GC","GT","GG"]
    #print("GC-content: %.4f"%(gc))
    db_static={}
    db_static_duo={}
    for nucl in sett:		
        #print("#%s = %d/%d"%(nucl,seq.count(nucl),len(seq)))
        db_static[nucl]=seq.count(nucl)/len(seq)
    for duo in sett_duo:
        db_static_duo[duo]=seq.count(duo)/len(seq)
    return db_static,gc,db_static_duo

"""				
def aminoacid_freq(file):
	op=open("./proteomes/"+file)
	sett="ACDEFGHIKLMNPQRSTVWY"
	diamino=[]	
	for one in sett:
		for two in sett:
			diamino.append(str(one)+str(two))
	
	seq=[]
	for line in op:
		if line.startswith(">./")==False:
			seq.append(line.strip())
	seq="".join(seq)
	op.close()
	print("Amino acid frequency:\n")
	for amino in sett:
		
		#print("#%s = %d/%d"%(amino,seq.count(str(amino)),len(seq)))
"""
	
#gc_content(sys.argv[1])
#print(nucl_freq(sys.argv[1]))
#aminoacid_freq(sys.argv[1])