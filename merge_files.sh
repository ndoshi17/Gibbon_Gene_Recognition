#!/bin/bash

####
# Takes an input directory name and an output file name as arguments
# Concatentaates the input files, but with only one header line at the top of the file.
# Assumes all input files have a one line header at the top of the file.
#
indir=outdirExons
indir2=outdir5UTR

outfile=gibbon_exon_feat_table.all.txt
outfile2=gibbon_5UTR_feat_table.all.txt

./cat_dir_with_header.pl $indir $outfile
./cat_dir_with_header.pl $indir2 $outfile2