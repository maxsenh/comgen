#script
import matplotlib
matplotlib.use("Agg")
import gzip
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

def calculate_average(path):
	for i in range(1,6):
		op=open(path+"file"+str(i)+".txt")
		cnt=0
		s=set()		
		for line in op:
			gen_a,gen_b,score=line.split()
			s.add(gen_a)
			cnt=cnt+1
		print("File: %s, Number of Genes: %d, Number of Interactions: %d, Average connectivity: %.4f"%(i,len(s),cnt,cnt/len(s)))
	
def quest2(file):
    op=open("../../protlinks/"+file)
    genelist=[]
    for line in op:
        genea,geneb,score=line.split()
        genelist.append(genea)
    dbx=Counter(genelist)
    dby=Counter(dbx.values())
    a=np.asarray(list(dbx.values()))
    plt.hist(a,normed=0)
    plt.savefig("out"+str(file)[4:5]+".png")
    
#calculate_average("./quest1/")    
[quest2("file"+str(i)+".txt") for i in range (1,7)]

			















		