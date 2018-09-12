$CLASS_DIR: /ACTF/Course/igb_s18

Shell Script Command Line Order:
1. splitFiles.sh
2. submit.sh
3. merge_files.sh
4. call_quick_svm.sh

Description of Shell Script Operations:
1. Splits original large fasta files into smaller more managable files using python.
2. Submits the split files to compute features using sungrid engine, a computing cluster, to allow for parallel processing of the files. Features are computer using pyhton.
3. Combines the feature files formatted to be used in the SVM using perl.
4. Inputs the complete feature files into the SVM which uses liblineaR to train a model and produce an accuracy. (Uses 80% to train and 20% to test)


All folders and files needed will be created by the scripts if they do not already exist otherwise files will be overwritten by the scripts.
