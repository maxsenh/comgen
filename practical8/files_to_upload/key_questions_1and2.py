#script
import matplotlib
matplotlib.use("Agg")
from collections import Counter
import matplotlib.pyplot as plt
import sys


def quest1(path):
	for i in range(1,6):
		op=open(path+"file"+str(i)+".txt")
		cnt=0
		s=set()		
		for line in op:
			gen_a,gen_b,score=line.split()
			s.add(gen_a)
			cnt=cnt+1
		print("File: %s, Number of Genes: %d, Number of Interactions: %d, Average connectivity: %.4f"%(i,len(s),cnt,cnt/len(s)))
	
def quest2(files):
    op=open("../../protlinks/"+files)
    genelist=[]
    for line in op:
        genea,geneb,score=line.split()
        genelist.append(genea)
    dbx=Counter(genelist)
    dby=Counter(dbx.values())
  
    plt.scatter(list(dby.keys()),list(dby.values()))			
    plt.ylabel("frequency of node degree")
    plt.xlabel("node degree")
    plt.title("out - "+str(files))
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig("out"+str(files)[4:5]+".png")
    
#quest1("../../protlinks/")    
#quest2(sys.argv[1])
			















		
