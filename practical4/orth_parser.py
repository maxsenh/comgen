#top hit parser

#for reference genome, extract the 3 orthologues from each of the other 3 folders, which match the ORF.

def orth_parser(file1, file2, file3, file4):
    ORF16_list = []
    ref20list = []
    ref44list = []
    ref47list =[]
    orth_parsed = open(file1 + 'orth_parsed', 'w')
    with open(file1) as ref1:
        for line in ref1:
            a = './16.fa.txt' + line.split("./16.fa.txt")[1].split(" ")[0]
            ORF16_list.append(a)
    with open(file2) as que1:
        for line in que1:
            ref20list.append(line.split(" "))

    with open(file3) as que2:
        for line in que2:
            ref44list.append(line.split(" "))

    with open(file4) as que3:
        for line in que3:
            ref47list.append(line.split(" "))
    
    for orths in ORF16_list:
        for items in ref20list:
            for item in items:
                if item in ORF16_list:
                    #print(item + items[2])
                    orth_parsed.write(item + " ")
                    orth_parsed.write(items[2] + " ")
        for items in ref44list:
            for item in items:
                if item in ORF16_list:
                    orth_parsed.write(items[2] + " ")
        for items in ref47list:
            for item in items:
                if item in ORF16_list:
                    orth_parsed.write(items[2] + "\n ")
        
    
    #aa = set(ref20list).intersection(ORF16_list)
    #print(aa)
    #print(ORF16_list)
    #print(ref20list)
    #print(ref47list)
    
    """for items in ref20list:
        for item in items:
            if item in ORF16_list:
                orth_parsed.write(item + " ")
                orth_parsed.write(items[2] + " ")"""
    
    
    
    
    
    
    
if __name__ == "__main__":
    orth_parser('1_5_output/r16_20', '1_5_output/r16_20', '1_5_output/r16_44', '1_5_output/r16_47')