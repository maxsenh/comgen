#simple file parser for genscan

file1 = open('Genscan_peptide', 'r').striplines()
file2 = open('Genscan_all', 'r')

peptide_headers = []

for line in file1:
	if '


