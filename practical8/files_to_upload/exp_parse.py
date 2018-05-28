# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:05:38 2018

@author: u2359
"""

def exp_parse (file_handle):
    exp_list = []
    exp_dict = {}
    with open (file_handle) as f:
        for line in f:
            entries = (line.strip("\n").split(" "))
            exp_list.append(entries)
    #print (exp_list)
    for i in range(len(exp_list)):
        exp_dict [i] = exp_list[i]
    return (exp_dict)

def blast_out_parse (file_handle):
    with open (file_handle) as f:
        line_list = []
        gene_symbol_lst = []
        for line in f:
            line_list.append(line)
        for entry in line_list:
            if entry.startswith("./"):
                #print(entry)
                #e = re.search('sp|(.*)_Y', entry)
                ee = (entry.split('sp|'))[1].split('_Y')[0]
                gene_symbol_lst.append(ee[7::])
            
        return (gene_symbol_lst)

def overlap_count():
    overlap_dict = {}        
    writefile = open('outID52', 'w')
    for IDs, sets in exp_dict.items():
        #print(sets)
        count = 0
        for genes in sets:
            if genes in gene_symbol_lst:
                count += 1
                overlap_dict [IDs] = count
        #writefile.write ('ID:' + str(IDs) + '  count:' + str(count) + ':' + str(exp_dict[IDs]) + '\n')
    #print(overlap_dict)
    for IDs, sets in exp_dict.items():
        if IDs == 52:
            for items in sets:
                writefile.write(items + '\n')
                
        

if __name__ == "__main__":
    exp_dict = exp_parse ('experiments.txt')
    gene_symbol_lst = blast_out_parse ('outblastp')    
    overlap_count()