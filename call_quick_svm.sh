#!/bin/bash
export R_LIBS=$R_LIBS:/local/cluster/R_Packages/3.3

class1Examples=gibbon_exon_feat_table.all.txt
class2Examples=gibbon_5UTR_feat_table.all.txt


Rscript quick_svm.R $class1Examples $class2Examples
