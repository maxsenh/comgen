#script
import gzip




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
calculate_average("./quest1/")
