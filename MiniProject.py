import os
#problem 1

path = "export PATH=$PATH:$PWD/sratoolkit.2.11.2-ubuntu64/bin" #preparing command to set sratoolkit/bin as path enivornmnet variable

os.system(path) #setting sratoolkit/bin as path eniornment table
sra_id = "SRR8185310" #set the run to download 
prefetch = "prefetch " + sra_id #prepare command 
os.system(prefetch) #send command to linux commmand line


fastq_dump = "fastq-dump -I --split-files " + sra_id #prepare command
os.system(fastq_dump) # send command to linux command line


#Problem 2
path = "export PATH=$PATH:$PWD/SPAdes-3.12.0-Linux/bin"
os.system(path) #setting SPAdes/bin as path enviornment variable
SPAdes = "spades.py -s " + sra_id + "_1.fastq" + " -o $HOME/spades_run1"
os.system(SPAdes)
  
