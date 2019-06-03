# Bioinformatics
Bioinformatics Projects
This folder includes my volunteery small projects accomplished at GSC along with some other small projects
GSC volunteery mini projects: GSC.py , sequence.p, stat.py
Other small projects: GSC_Content , K-mer 

gsc.py:
    #This Python script creates 2 lists from a data file I have.
    One list will contain all the files that start with the term ‘stats’ in it.
    The second list will contain all files that have the term ‘thresholds.bbt.db’ in it. 


sequence.py:
     #The input file has about 7,000 sequences. it contains 3 comma-separated fields: candidate id, sequence and status.  Each      line represents a different candidate sequence.  
     This python script will scan each sequence and check for monomeric nucleotide repeats (mnr) of 8 or more. After finding        a sequence that matches that criteria, it will write entire row into a new output file (with all 3 fields).
     lastly this program also calculate the number ofsequneces that contain mnr and also those mnr sequences that have a “yes      in the third column.
     

stat.py:
     #I am comparing the 5 and 95 percentile of 2 files which are the results of shotgun sequencing in different period of          time. Only the lines starting with the term "dataline" needs to be compared.
     lines starting with the term dataline have 7 columns.
     In this Python script I used dictionary and CSV reader in order to compare these numbers and giving out the difference        between them.
     
 
 GSC_Content:
     #find GC content of brca1 gene
     brca1 gene is the one for breast cancer
     downloading the FASTA format of the gene from NCBI
     

K-mer:
    #Writting a Python program to count k-mers (substring of length k) in DNA sequencing data.
