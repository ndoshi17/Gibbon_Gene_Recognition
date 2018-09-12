import numpy
import sys
import os

def main():
	wholeFile = True
	arr = []

	file = sys.argv[1]
	outdir = sys.argv[2]

	seq = ''
	counter = 0
	with open(file) as f:
		for line in f.readlines():
			arr.append(line)
			

	
	print("Sequences: {}".format(len(arr)))
	C_G = 0
	count = 0
	CG_arr = []
	if(wholeFile == True):
		for sequence in arr:
			for c in sequence:
				if(c.lower() == "c" or c.lower() == "g"):
					C_G += 1
				count += 1
			prcnt = (float(C_G)/count)*100
			CG_arr.append(prcnt)
			C_G = 0
			count = 0

	else:
		for line in range(100):
			for c in arr[line]:
				if(c.lower() == "c" or c.lower() == "g"):
					C_G += 1
				count += 1
			prcnt = (float(C_G)/count)*100
			CG_arr.append(prcnt)
			C_G =0
			count =0		

	#start codons
	atg_count = 0;
	atg_arr = [];
	#stop codons
	uaa_count = 0;
	uaa_arr = [];
	uag_count = 0;
	uag_arr = [];
	uga_count = 0;
	uga_arr = [];	
	
	for sequence in arr:
		for c in range(len(sequence)-3):
			if(sequence[c:c+3] == 'ATG'):
				atg_count += 1
			if(sequence[c:c+3] == 'TAA'): #UAA
				uaa_count += 1
			if(sequence[c:c+3] == 'TAG'): #UAG
				uag_count += 1
			if(sequence[c:c+3] == 'TGA'): #UGA
				uga_count += 1
		atg_arr.append((float(100*atg_count)/len(sequence)));
		atg_count =0;
		uaa_arr.append((float(100*uaa_count)/len(sequence)));
		uaa_count =0;
		uag_arr.append((float(100*uag_count)/len(sequence)));
		uag_count =0;
		uga_arr.append((float(100*uga_count)/len(sequence)));
		uga_count =0;

	tata_count = 0;
	tata_arr = [];
	for sequence in arr:
		for c in range(len(sequence)-4):
			if(sequence[c:c+4] == 'TATA'):
				tata_count += 1
		tata_arr.append((float(100*tata_count)/len(sequence)));
		tata_count =0;

#codons make a table of codons
#start
#AUG
#stop
#UAA
#UAG
#UGA

	

	num = file[file.find('.')+1:len(file)]
	if not (os.path.exists(outdir)):
		os.mkdir(outdir)
	with open(outdir+"/feature_file.%s" % num, "w") as out:
		out.write("Seqid\tGCcont\tATGfreq\tUAAfreq\tUAGfreq\tUGAfreq\tTATAfreq\n") #
		for i in range(0,len(arr)):
			out.write("Seq%s%s\t" %(num, i))
			out.write("%s\t" % CG_arr[i])
			out.write("%s\t" % atg_arr[i])
			out.write("%s\t" % uaa_arr[i])
			out.write("%s\t" % uag_arr[i])
			out.write("%s\t" % uga_arr[i])
			out.write("%s" % tata_arr[i])
			out.write("\n")


main()
