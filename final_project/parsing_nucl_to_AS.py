
#Amino acid sequence handling
###########################################################################

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord   

###########################################################################
# Translation of nucleotide-ORFs to amino-acid-sequence ORFs
###########################################################################
def translate_orf(listin):
	for i in listin:
		op=open("proteome"+str(i)+".fasta","w")
		#extracting only the sequences from the fasta files
		#using BIOpython for translation
		for rec in SeqIO.parse("out_orf"+str(i)+".fasta","fasta"):
			seq=rec.seq
			aminos=seq.translate()
			amino_rec=SeqRecord(aminos, id=rec.id,description="")
			#writing the sequences with their titles into a file			
			SeqIO.write(amino_rec,op,"fasta")
		op.close()


###########################################################################
# Calling functions
###########################################################################	

translate_orf(["00","16","20","29","44","47"])

###########################################################################
#
###########################################################################
