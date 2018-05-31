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

def nucl(one,two):
    return math.sqrt(sum([(one[i]-two[i])**2 for i in range (len(one))]))

def dist(list_of_in):
    gc_list=[]
    nucl_freq_list=[]
    nucl_freq_duo=[]
    for i in list_of_in:
        db_static,gc,db_static_duo=nucl_freq(str(i)+".fa.txt")
        nucl_freq_list.append(list(db_static.values()))
        gc_list.append(gc)
        nucl_freq_duo.append(list(db_static_duo.values()))
    #GC-content yo
    mat_GC=np.zeros(shape=(len(gc_list),len(gc_list)))
    for x in range(0,len(gc_list)):
        for y in range(0,len(gc_list)):
            mat_GC[x,y]=float(abs((gc_list[x]-gc_list[y])*100))
    print([i for i in list_of_in])									
    print("gc\n",mat_GC)
    #np.savetxt("gc_content_dist_matrix.grimm",np.asarray([float(i) for i in list_of_in]))
    np.savetxt("trial_gc_content_dist_matrix.grimm",mat_GC,fmt="%.5f")
    #with open("gc_content_dist_matrix.grimm", "a") as myfile:
    #    myfile.write("16 20 29 44 47")
    
    #solo nucl-yo
    mat_dist=np.zeros(shape=(len(nucl_freq_list),len(nucl_freq_list)))
    for x in range(0,len(nucl_freq_list)):
        for y in range(0,len(nucl_freq_list)):
            mat_dist[x,y]=nucl(nucl_freq_list[x] * 100,nucl_freq_list[y] * 100)
    print("solo nucl\n",mat_dist)
    np.savetxt("nucl_freq_dist_matrix.grimm",mat_dist,fmt="%.5f")
    
    #duo nucl-yo
    mat_dist_duo=np.zeros(shape=(len(nucl_freq_duo),len(nucl_freq_duo)))
    for x in range(0,len(nucl_freq_duo)):
        for y in range(0,len(nucl_freq_duo)):
            mat_dist_duo[x,y]=nucl(nucl_freq_duo[x] * 100,nucl_freq_duo[y] * 100)
    print("duo nucl\n",mat_dist_duo)
    np.savetxt("dinucl_freq_dist_matrix.grimm",mat_dist_duo,fmt="%.5f")
    
dist(["16","20","29","44","47"])
#dist(["00","47"])#,"16","20","29","44","47"])
