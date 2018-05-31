#dist calculator

import sys
import os
import math
import numpy as np

def gc_content():
    title = ""
    seq = ""
    path = "genomes/"
    gc_dict = {}
    file_list = os.listdir (path)
    gc_names = []
    gc_list = []
    for files in file_list:
        if files.endswith('.fa.txt'):
            gc_names.append(files)
            #print(file)
            with open (path + files) as f:
                for line in f:
                    if line.startswith(">./"):
                        title = line
                    else:
                        seq = line
        gc = (seq.count("C") + seq.count("G"))/len(seq)
        #print (str(title) + str(gc))
        gc_dict[title.rstrip()] = gc
        gc_list.append(gc)
    gc_array = np.asarray(gc_list)
    print(gc_array)
    return (gc_dict), gc_names, gc_array
    
def dist_calc():
    """run_list = [1, 2]
    dist_list = []
    for i in run_list:
        name = ">./" + (gc_names[i])
        if name in gc_dict.keys():
            dist_list.append(gc_dict[name])
    #print(dist_list)
    for dist in range (len(dist_list)):
        diff = dist_list[0] - dist_list[1]
    print(diff)"""
    gc_diff = np.zeros((len(gc_array), len(gc_array)))
    for x in range (0, len(gc_array)):
        for y in range (0, len(gc_array)):
            gc_diff [x, y] = gc_array[x] - gc_array[y]
            
    print (gc_diff)    
    
if __name__ == "__main__":
    gc_dict, gc_names, gc_array = gc_content()
    dist_calc()