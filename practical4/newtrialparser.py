import sys
import re
from Bio.Blast import NCBIXML

file_handle = sys.argv [1]

blastOutputXMLHandle = open (file_handle)
output_file = open(file_handle + '_output', 'w')

Alignment_titles = []
Query_list = []
Hit_list = []

for listOfBlastRecords in NCBIXML.parse (blastOutputXMLHandle):

	for alignments in listOfBlastRecords.alignments:
		for hsp in alignments.hsps:
			Alignment_titles.append(alignments.title)
			Query_list.append(hsp.query)
			Hit_list.append(hsp.sbjct)
#print(Alignment_titles)
hit_names=[]
query_names=[]
for s in Alignment_titles:
	ii=s.split("./")
	hit_names.append(ii[0])
	query_names.append(ii[1])

for i in range(len(hit_names)):
		print(query_names[i]+" "+Query_list[i]+" "+hit_names[i]+" "+Hit_list[i])

# To extract: Hit_id, Hit_def, HSP_qseq:query, HSP_hseq:sbjct