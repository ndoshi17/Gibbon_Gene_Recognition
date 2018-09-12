#!/bin/bash
#$ -S /bin/bash
#$ -V
#$ -N TEST_Doshi
#$ -cwd
#$ -o test_doshi.log
#$ -j y
#$ -t 1-10:1

./computeFeatures.sh $SGE_TASK_ID outdirExons
