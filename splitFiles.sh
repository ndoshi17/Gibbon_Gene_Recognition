#!/bin/bash

indir=originalFastaFiles/gibbonExons.txt
indir2=originalFastaFiles/gibbon5UTR.txt
numFiles=10
outdir=Split_Files_FolderExons
outdir2=Split_Files_FolderUTR

python file_splitter.py $indir $numFiles $outdir

python file_splitter.py $indir2 $numFiles $outdir2