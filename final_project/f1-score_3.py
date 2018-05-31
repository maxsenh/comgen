
# Compute F1-score to access the performance of the predictor
###########################################################################

from Bio import SeqIO
import sys

###########################################################################
# F1 
###########################################################################
def f1_score(pred_file,ref_file):

	#parsing the amino acid sequences (genes) from the reference
	#and the predicted proteomes	
	all_sequences_pred=[rec.seq for rec in SeqIO.parse(pred_file,"fasta")]
	all_sequences_ref=[rec.seq for rec in SeqIO.parse(ref_file,"fasta")]

	#computing the true positives, the false positives and the 
	#false negatives	
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
	
	#computation of precision and recall, which are required for the
	#F1-score
	prec=len(list_tp)/(len(list_tp)+len(list_fp))
	reca=len(list_tp)/(len(list_tp)+len(list_fn))
	f1_score=2*((prec*reca)/(prec+reca))
	
	#printing the results
	print("true positives: %d, false positives: %d, false negative: %d"%(len(list_tp),len(list_fp),len(list_fn)))
	print("F1-score: %.4f"%(f1_score))	
	print("len pred: %d, len ref: %d"%(len(all_sequences_pred),len(all_sequences_ref)))	

###########################################################################
# Functions
###########################################################################

inp=sys.argv[1]
f1_score("./predicted_proteomes/proteome"+str(inp)+".fasta","./proteomes/"+str(inp)+".fa.txt.pfa")

###########################################################################
# 
###########################################################################