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

def dist(file1,file2):
    db_static1,gc1=nucl_freq(file1)
    db_static2,gc2=nucl_freq(file2)
    print(gc1,gc2)
    print(db_static1)
    print(db_static2)
    #3
def plot_matrix(seq_0, seq_1):
    mat=np.zeros(shape=(len(seq_0),len(seq_1)))
    for x in range(0,len(seq_0)):
        for y in range(0,len(seq_1)):
            if seq_0[x]==seq_1[y]:
                mat[x,y]=1
    print(mat)
    #plt.matshow(mat)
    #plt.savefig("out.png")

plot_matrix("ABC","ABX")    
#dist(sys.argv[1],sys.argv[2])
