#script
import gzip




def extracting(path):
	names=["scerev","lgelid","nmenin","rbalti","tmarit"]
	ids=["4932","927691","122586","243090","243274"]
	db=dict(zip(ids,names))
	print(str(ids[0]))
	scerev=[]
	lgelid=[]
	nmenin=[]
	rbalti=[]
	tmarit=[]
	with gzip.open(path+"protein.links.v10.5.txt.gz","r") as f:
		for line in f:
			if line.startswith(b"4932"):
				scerev.append(line)
			if line.startswith(b"927691"):
				lgelid.append(line)
			if line.startswith(b"122586"):
				nmenin.append(line)
			if line.startswith(b"243090"):
				rbalti.append(line)
			if line.startswith(b"243274"):
				tmarit.append(line)
	
extracting("../../protlinks/")
			