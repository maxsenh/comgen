#simple genscan parser

with open('Genscan_peptide.txt', 'r') as file1:
    writefile = open('peptide_out', 'w')
    for line in file1:
        if ">" in line:
            #peptide_headers.append(line)
            writefile.write(line)
        if line.strip("\n").isupper():
            #peptide_seq.append(line)
            writefile.write(line)
    
with open('Genscan_all.txt', 'r') as file2:
    writefile1 = open('nucleotide_out', 'w')
    for line in file2:
        if ">" in line and line.endswith("bp\n"):
            #print(line)
            writefile1.write(line)
        if line.strip("\n").islower():
            #print(line)
            writefile1.write(line)

