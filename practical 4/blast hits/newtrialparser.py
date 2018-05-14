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
print(Hit_list)











# To extract: Hit_id, Hit_def, HSP_qseq:query, HSP_hseq:sbjct
