# -*- coding: utf-8 -*-
"""
Created on Wed May 30 16:28:47 2018

@author: u2362
"""

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

def translate_orf(listin):
	for i in listin:
		op=open("proteome"+str(i)+".fasta","w")
		for rec in SeqIO.parse("out_orf"+str(i)+".fasta","fasta"):
			seq=rec.seq
			aminos=seq.translate()
			amino_rec=SeqRecord(aminos, id=rec.id,description="")
			SeqIO.write(amino_rec,op,"fasta")
		op.close()
		
def freq_amino(listin):
	complete=[]	
	sett="ACDEFGHIKLMNPQRSTVWY"
	what=[]
	for i in listin:
		op=open("proteome"+str(i)+".fasta")
		s=[line.strip() for line in op if not line.startswith(">")]
		complete.append("".join(s))
		op.close()
	for element in complete:		
		listofone=[(element.count(str(a)+str(b)))/len(element) for b in sett for a in sett]
		what.append(listofone)
	print(what)
	print(len(what))	
#freq_amino(["00"])#,"16","20","29","44","47"])		
translate_orf(["00","16","20","29","44","47"])