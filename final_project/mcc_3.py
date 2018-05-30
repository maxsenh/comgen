# -*- coding: utf-8 -*-
"""
Created on Wed May 30 17:47:51 2018

@author: u2362
"""
from Bio import SeqIO

def mcc(pred_file,ref_file):
	all_sequences_pred=[rec.seq for rec in SeqIO.parse(pred_file,"fasta")]
	all_sequences_ref=[rec.seq for rec in SeqIO.parse(ref_file,"fasta")]
	tp=0
	tn=0
	fp=0
	fn=0
	for i in all_sequences_ref:
		if i in all_sequences_pred:
			tp=+1
	print(tp)
	print(len(all_sequences_pred),len(all_sequences_ref))	
"""
def mcc(listin):
	
	list_of_mcc=[]
	for one_file in listin:
	
"""
mcc("./predicted_proteomes/proteome20.fasta","./real_proteomes/prot20.fasta")