# -*- coding: utf-8 -*-
"""
Created on Fri May 25 16:47:28 2018

@author: u2362
"""

#3. Distance matrix tool
import matplotlib
matplotlib.use("Agg")
from stat_tool_1 import nucl_freq
import sys
import numpy as np
import matplotlib.pyplot as plt
import math

def dist(list_of_in):
    gc_list=[]
    nucl_freq_list=[]
    for i in list_of_in:
        nucl=[]
        db_static,gc=nucl_freq(str(i)+".fa.txt")
        nucl_freq_list.append(list(db_static.values()))
        gc_list.append(gc)

    #GC-content yo
    mat_GC=np.zeros(shape=(len(gc_list),len(gc_list)))
    for x in range(0,len(gc_list)):
        for y in range(0,len(gc_list)):
            mat_GC[x,y]=abs(gc_list[x]-gc_list[y])
    print([i for i in list_of_in])									
    print(mat_GC)
    #np.savetxt("gc_content_dist_matrix.grimm",np.asarray([float(i) for i in list_of_in]))
    np.savetxt("gc_content_dist_matrix.grimm",mat_GC)
    with open("gc_content_dist_matrix.grimm", "a") as myfile:
        myfile.write("16 20 29 44 47")


    '''
    #Nucleotide frequency
    mat_GC=np.zeros(shape=(len(gc_list),len(gc_list)))
    for x in range(0,len(gc_list)):
        for y in range(0,len(gc_list)):
            mat_GC[x,y]=math.sqrt((gc_list[x]-gc_list[y])**2)
    print([i for i in list_of_in])									
    print(mat_GC)
    '''

#plot_matrix("AB","AB")    
dist(["16","20","29","44","47"])
