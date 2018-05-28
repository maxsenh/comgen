#dist calculator

import sys
import os
import math

def gc_content():
    title = ""
    seq = ""
    path = "genomes/"
    gc_dict = {}
    file_list = os.listdir (path)
    gc_names = []
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
    return (gc_dict), file_list
    
def dist_calc():
    for i in range (len(gc_names)):
        print(gc_names[1])
    
if __name__ == "__main__":
    gc_dict, gc_names = gc_content()
    dist_calc()