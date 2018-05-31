
# Creating distance matrices
###########################################################################

import matplotlib
matplotlib.use("Agg")
from stat_tool_1 import nucl_freq
import numpy as np
import math

###########################################################################
# Computing of distance between two different matrices
###########################################################################
def nucl(one,two):
    return math.sqrt(sum([(one[i]-two[i])**2 for i in range (len(one))]))

###########################################################################
# Computing the distance matrix between all 5 genomes
###########################################################################
def dist(list_of_in):
	#three lists for: GC-content, nucleotide frequency, dinucleotide frequency
    gc_list=[]
    nucl_freq_list=[]
    nucl_freq_duo=[]
	
	#using the function "nucl_freq" from the statistic tool to obtain frequency
	#of each of the genomes
    for i in list_of_in:
        db_static,gc,db_static_duo=nucl_freq(str(i)+".fa.txt")
        nucl_freq_list.append(list(db_static.values()))
        gc_list.append(gc)
        nucl_freq_duo.append(list(db_static_duo.values()))

								
    #Distance matrix for GC-content
    #create numpy matrix
    mat_GC=np.zeros(shape=(len(gc_list),len(gc_list)))
    for x in range(0,len(gc_list)):
        for y in range(0,len(gc_list)):
									
	       #equation for the distance 
            mat_GC[x,y]=float(abs(gc_list[x]-gc_list[y]))								

    #print and save the matrix to a file
    print("gc\n",mat_GC)
    np.savetxt("gc_content_dist_matrix.grimm",mat_GC,fmt="%.5f")


    #Distance matrix for nucleotide frequency
    #create numpy matrix
    mat_dist=np.zeros(shape=(len(nucl_freq_list),len(nucl_freq_list)))
    for x in range(0,len(nucl_freq_list)):
        for y in range(0,len(nucl_freq_list)):
									
	       #equation for the distance, using the function nucl from above
            mat_dist[x,y]=nucl(nucl_freq_list[x],nucl_freq_list[y])

    #print and save the matrix to a file
    print("solo nucl\n",mat_dist)
    np.savetxt("nucl_freq_dist_matrix.grimm",mat_dist,fmt="%.5f")

    
    #Distance matrix for dinucleotide frequency
    #create numpy matrix
    mat_dist_duo=np.zeros(shape=(len(nucl_freq_duo),len(nucl_freq_duo)))
    for x in range(0,len(nucl_freq_duo)):
        for y in range(0,len(nucl_freq_duo)):
									
	       #equation for the distance, using the function nucl from above
            mat_dist_duo[x,y]=nucl(nucl_freq_duo[x],nucl_freq_duo[y])

    #print and save the matrix to a file
    print("duo nucl\n",mat_dist_duo)
    np.savetxt("dinucl_freq_dist_matrix.grimm",mat_dist_duo,fmt="%.5f")
    
###########################################################################
# Functions
###########################################################################
				
dist(["16","20","29","44","47"])

###########################################################################
#
###########################################################################
