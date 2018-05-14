def FASTA_finder(filename):

    header_list = []
    seq_list = []
    dict16 = {}
    dict20 = {}
    dict44 = {}
    dict47 = {}
    bigdict = {}
    with open("new/new_16.txt.pfa") as db16:
        for line in db16:
            if ">" in line:
                header_list.append(line)
            if line.isupper():
                seq_list.append(line)
        for i in range(len(header_list)):
            bigdict[header_list[i].strip("\n")] = seq_list[i]
    
    with open("new/new_20.txt.pfa") as db16:
        for line in db16:
            if ">" in line:
                header_list.append(line)
            if line.isupper():
                seq_list.append(line)
        for i in range(len(header_list)):
            bigdict[header_list[i].strip("\n")] = seq_list[i].strip("\n")
    
    with open("new/new_44.txt.pfa") as db16:
        for line in db16:
            if ">" in line:
                header_list.append(line)
            if line.isupper():
                seq_list.append(line)
        for i in range(len(header_list)):
            bigdict[header_list[i].strip("\n")] = seq_list[i].strip("\n")
    
    with open("new/new_47.txt.pfa") as db16:
        for line in db16:
            if ">" in line:
                header_list.append(line)
            if line.isupper():
                seq_list.append(line)
        for i in range(len(header_list)):
            bigdict[header_list[i].strip("\n")] = seq_list[i].strip("\n")

    #print(bigdict)

    
    cluster_raw_list = []
    with open(filename, 'r') as f:
        for line in f:
            cluster_raw_list.append(line.split(" ./"))
            
    #print(cluster_raw_list)
    
    for i in range(len(cluster_raw_list)):
        FASTA_cluster = open('FASTA_cluster' + str(i), 'w')
        #print(cluster)
        for fake_orf in cluster_raw_list[i]:
            #print(fake_orf.strip("./ /n"))
            if (">./" + fake_orf.strip("./ \n")) in bigdict:
                FASTA_cluster.write(fake_orf.strip("./ \n") + "\n")
                FASTA_cluster.write(bigdict[">./" + fake_orf.strip("./ \n")] + "\n")
            #cluster_raw_list.append(line.split("./"))
    """flat_cluster_list = [item for sublist in cluster_raw_list for item in sublist]
    cluster_list = []
    for item in flat_cluster_list:
        #item.strip("./")
        cluster_list.append(item.strip("./ \n"))
    #print(cluster_list)
    for orf in cluster_list:
        if (">./" + orf) in bigdict:
            #print(orf)
            FASTA_cluster.write(orf + "\n")
            FASTA_cluster.write(bigdict[">./" + orf] + "\n")"""
    #if '>./47.fa.txt_orf04524' in bigdict:
    #    print('yes')


#>./47.fa.txt_orf04524


if __name__ == "__main__":
    FASTA_finder('1_5_output/10_orth_parsed.txt')