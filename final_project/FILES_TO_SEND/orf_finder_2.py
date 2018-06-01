
# Prediction of ORFs with given genomes 
###########################################################################
import sys

###########################################################################
# ORF-finder
###########################################################################

def orf_finder(infile,outfile):
	
	#stripping the sequence from the title
	op=open(infile)
	seq=""
	stop=["TGA","TAA","TAG"]	#stop codons
	orf_list=[]	
	for line in op:
		if not line.startswith(">./"):
			seq=line.strip()
	
	#finding ORFs on the template strand from 5´->3´
	for j in range(3):		#creating three different reading frames
		t=0				#is used to remove the overlapps
		for i in range(j,len(seq)-1,3):		#sliding window of 3
			if seq[i-1:i+2] == "ATG" and i > t: 		#finding start-codon			
				mid=[]
				for f in range(i-1,len(seq),3):		#appending to list
					if seq[f:f+3] in stop:
						break      #break if stop-codon is encountered
					else:
						t=f				
					if len(seq[f:f+3])==3:
						mid.append(seq[f:f+3])
				joined="".join(mid)
				#if found sequence is within the size limitation it will
				#be added to the master list orf_list
				#for prokaryots:
				#if len(joined) > 300:
				#for eukaryotes:
				#if len(joined) > 150 and len(joined) < 1500:
				if len(joined) > 300:
					orf_list.append(joined)
					
	#the same is done with the reverse strand
	complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A','N':'N'}
	s=(''.join([complement[base] for base in seq[::-1]]))
	rev_list=[]
	for j2 in range(3):
		t2=0		
		for i2 in range(j2,len(s)-1,3):
			if s[i2-1:i2+2] == "ATG" and i2 > t2:
				mid=[]
				for f2 in range(i2-1,len(s),3):				
					if s[f2:f2+3] in stop:
						break					
					else:
						t2=f2
						if len(s[f2:f2+3])==3:
							mid.append(s[f2:f2+3])
				joined="".join(mid)
				if len(joined) > 300:
					rev_list.append(joined)
    #printing to test the number of found orfs
	print("Number of template ORFs: %d, Number of reverse ORFs: %d"%(len(orf_list),len(rev_list)))
	print("Number of total ORFs: %d"%(len(orf_list)+len(rev_list)))
	#writing the orfs from both strands in a file
	wr=open(outfile,"w")
	for w in range(len(orf_list)):
		wr.write(">file_"+str(infile)+"_orf_"+str(w)+"\n")
		wr.write(orf_list[w]+"\n")
	for w_rev in range(len(rev_list)):
		wr.write(">file_"+str(infile)+"_orf_"+str(w_rev)+"_rev\n")
		wr.write(rev_list[w_rev]+"\n")
	wr.close()
	op.close()
###########################################################################
# Functions
###########################################################################
if __name__ == "__main__":
	#Run this for ORF-predition of given input genome 
	#Input: input genome file (which should be in fasta format) 
	#and desired output file (which will be in fasta format)
	#orf_finder(sys.argv[1],sys.argv[2])

###########################################################################
# 
###########################################################################

