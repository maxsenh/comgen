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
	
#calculate_average("./quest1/")

def quest2(file):
	op=open("./quest1/"+file)

	genset=set()
	genlist=[]
	for line in op:
		print(line)
		gen_a,gen_b,score=line.split()
		genset.add(gen_a)
		genlist.append(gen_a)
	countlist=[]
	for element in genset:
		count=0
		if element in genlist:
			count=count+1
		countlist.append(count)
	print(countlist)
quest2("file6.txt")

			















		