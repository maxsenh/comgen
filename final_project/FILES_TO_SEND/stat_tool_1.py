
# 1.1 Statistical tool
###########################################################################

import sys

###########################################################################
# Calculating the GC_content
###########################################################################
def gc_content(infile):
	op=open(infile)
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
def nucl_freq(infile):
    gc,seq=gc_content(infile)
    sett=str("".join(set(seq)))
    sett_duo=str("".join(set(seq)))
    db_static={}
    db_static_duo={}
    for nucl in sett:		
        #print("#%s = %d/%d"%(nucl,seq.count(nucl),len(seq)))
        db_static[nucl]=seq.count(nucl)/len(seq)
    for duo in sett_duo:
        db_static_duo[duo]=seq.count(duo)/(len(seq)-1)
    return db_static,gc,db_static_duo

###########################################################################
# Writing the (di-)nucleotide frequency to a file
###########################################################################
def write_nucl(infile,outfile):
	db_static,gc,db_static_duo=nucl_freq(infile)
	with open(outfile,"w") as ou:
		ou.write("GC-content: %.4f\nNucleotide Frequency:\n"%(gc))
		[ou.write("#%s = %.6f\n"%(i,db_static[i])) for i in db_static]
		ou.write("Dinucleotide Frequency:\n")
		[ou.write("#%s = %.9f\n"%(i,db_static_duo[i])) for i in db_static_duo]
		
###########################################################################
# Calculating the amino-acid frequency from a given proteome
###########################################################################
def aminoacid_freq(infile,outfile):
	op=open(infile)
	seq=[]
	seq=[line.strip() for line in op if not line.startswith(">")]
	seq="".join(seq)
	op.close()
	sett=str("".join(set(seq)))
	print(sett,len(sett))
	with open(outfile,"w") as ou:
		ou.write("Amino acid frequency:\n")
		#calculating amino acid frequency
		listof_freq=[seq.count(a)/len(seq) for a in sett]
		[ou.write("#%s = %.6f \n"%(sett[a],listof_freq[a])) for a in range(len(listof_freq))]		
		#counting the diamino acid frequency from the long string of amino acids		
		listofduo=[(seq.count(str(a)+str(b)))/(len(seq)-1) for a in sett for b in sett]
		#creating the names of diaminos
		listofnames=[(str(a)+str(b)) for a in sett for b in sett]
		#writing diamino names and the corresponding frequency
		ou.write("Diamino acid frequency\n")
		[ou.write("#%s = %.6f\n"%(listofnames[i],listofduo[i])) for i in range(len(listofduo))]

###########################################################################
# Computes diamino-frequency from given proteome
###########################################################################
def freq_amino(listin):
	#string of all amino acids
	sett="ACDEFGHIKLMNPQRSTVWY"
	for i in listin:
		op=open("../predicted_proteomes/proteome"+str(i)+".fasta")
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
		outt=open("./diamino_out_"+str(i)+".txt","w")
		[outt.write("#%s = %.9f\n"%(listofnames[i],listofone[i])) for i in range(len(listofone))]
		outt.close()
				
###########################################################################
# Functions
###########################################################################	
if __name__ == "__main__":
	#Run this for (di)nucleotide frequency, input has to be the desired
	#input genome file and output file
	#write_nucl(sys.argv[1],sys.argv[2])

	#Run this for (di)amino acid frequency, input has to be the desired
	#input proteome file and output file
	aminoacid_freq(sys.argv[1],sys.argv[2])


#-----Test/helping scripts------
	#gc_content(sys.argv[1])
	#nucl_freq(sys.argv[1])
	#freq_amino(["16","20","29","44","47"])
	
###########################################################################

###########################################################################
