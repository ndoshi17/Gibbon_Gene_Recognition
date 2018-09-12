#!/bin/bash
task_id=$1
outdir=$2

python findFeatures.py Split_Files_FolderExons/Split_File.$task_id $outdir

python findFeatures.py Split_Files_FolderUTR/Split_File.$task_id outdir5UTR