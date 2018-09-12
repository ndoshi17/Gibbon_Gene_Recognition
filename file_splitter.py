#!/local/cluster/bin/python

#from Bio import SeqIO
import os
import glob
import numpy
import sys



def splitWriteFiles(seqList, numFiles, outdir):
	firstIdx = 0
	secondIdx = 1
	splitVal = (len(seqList)/numFiles)
	if(len(seqList)%numFiles != 0):
		splitVal+1
	if not (os.path.exists(outdir)):
		os.mkdir(outdir)
	for x in range(numFiles):
		with open(outdir+"/Split_File.%s" % (x+1),"w") as f:
			firstRange = splitVal * firstIdx
			secondRange = splitVal * secondIdx
			for i in range(firstRange, secondRange, 1):
				if(i < len(seqList)):
					f.write("%s\n" % seqList[i])
			firstIdx += 1
			secondIdx += 1

def main():

	file = sys.argv[1]
	numFiles = sys.argv[2]
	outdir = sys.argv[3]
	seqList = []
	last = 1

	seq = ''
	counter = 0
	with open(file) as f:
		for line in f.readlines():
			if(line[0] != '>'):
				if "Sequence" in line:
					last = 0
					continue
				last = 1
				seq += line[:-1]
			
			else:
				if(last == 1):
					counter+=1
					seqList.append(seq)
					seq = ''
	seqList.append(seq)

	seqList = seqList[1:]


	splitWriteFiles(seqList, int(numFiles), outdir)

main()