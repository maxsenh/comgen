# -*- coding: utf-8 -*-
"""
Created on Wed May 30 17:47:51 2018

@author: u2362
"""
from Bio import SeqIO
import sys

def f1_score(pred_file,ref_file):
	all_sequences_pred=[rec.seq for rec in SeqIO.parse(pred_file,"fasta")]
	all_sequences_ref=[rec.seq for rec in SeqIO.parse(ref_file,"fasta")]
	list_tp=[]
	list_fp=[]
	list_fn=[]
	for i in all_sequences_pred:
		if i in all_sequences_ref:
			list_tp.append(i)
		else:
			list_fp.append(i)
	for i in all_sequences_ref:
		if i not in all_sequences_pred:
			list_fn.append(i)

	prec=len(list_tp)/(len(list_tp)+len(list_fp))
	reca=len(list_tp)/(len(list_tp)+len(list_fn))
	f1_score=2*((prec*reca)/(prec+reca))
	print("true positives: %d, false positives: %d, false negative: %d"%(len(list_tp),len(list_fp),len(list_fn)))
	print("F1-score: %.4f"%(f1_score))	
	print("len pred: %d, len ref: %d"%(len(all_sequences_pred),len(all_sequences_ref)))	
"""
def mcc(listin):
	
	list_of_mcc=[]
	for one_file in listin:
	
"""
inp=sys.argv[1]
f1_score("./predicted_proteomes/proteome"+str(inp)+".fasta","./proteomes/"+str(inp)+".fa.txt.pfa")