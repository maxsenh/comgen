
# 1.1 Statistical tool
###########################################################################

import sys

###########################################################################
# Calculating the GC_content
###########################################################################
def gc_content(file):
	op=open("./genomes/"+file)
	seq=""
	for line in op:
		if not line.startswith(">./"):
			seq=line
	op.close()
	gc=(seq.count("C")+seq.count("G"))/len(seq)
	return gc,seq

###########################################################################
# Calculating the nucleotide- and dinucleotide-frequecy
###########################################################################
def nucl_freq(file):
    gc,seq=gc_content(file)
    sett=["A","C","G","T","N"]
    sett_duo=["AA","AC","AT","AG","CA","CC","CT","CG","TA","TC","TT","TG","GA","GC","GT","GG"]
    db_static={}
    db_static_duo={}
    for nucl in sett:		
        #print("#%s = %d/%d"%(nucl,seq.count(nucl),len(seq)))
        db_static[nucl]=seq.count(nucl)/len(seq)
    for duo in sett_duo:
        db_static_duo[duo]=seq.count(duo)/len(seq)
    return db_static,gc,db_static_duo

###########################################################################
# Calculating the amino-acid frequency from a given proteome
###########################################################################
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
		print("#%s = %d/%d, %.2f"%(amino,seq.count(str(amino)),len(seq),seq.count(str(amino))/len(seq)))

###########################################################################
# Computes diamino-frequency from given proteome
###########################################################################
def freq_amino(listin):
	#string of all amino acids
	sett="ACDEFGHIKLMNPQRSTVWY"
	for i in listin:
		op=open("proteome"+str(i)+".fasta")
		#extracting only the amino acids from the fasta file 
		s_unjoined=["".join(line.strip()) for line in op if not line.startswith(">")]
		op.close()
		s="".join(s_unjoined)		
		#counting the diamino acid frequency from the long string of amino acids		
		listofone=[(s.count(str(a)+str(b)))/len(s) for a in sett for b in sett]
		print(listofone)
		#creating the names of diaminos
		listofnames=[(str(a)+str(b)) for a in sett for b in sett]
		#writing diamino names and the corresponding frequency
		outt=open("./FILES_TO_SEND/diamino_out_"+str(i)+".txt","w")
		[outt.write("%s %.9f\n"%(listofnames[i],listofone[i])) for i in range(len(listofone))]
		outt.close()
				
###########################################################################
# Functions
###########################################################################	
	
#gc_content(sys.argv[1])
#print(nucl_freq(sys.argv[1]))
#aminoacid_freq(sys.argv[1])
#freq_amino(["16","20","29","44","47"])
	
###########################################################################

###########################################################################