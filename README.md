# Mini-Project
COMP 383 mini-project. Create a wrapper to integrate and execute the automation of software tools. 


# Problem 1:  Retrieve the Illumina reads for the resequencing of K-12 project:
https://www.ncbi.nlm.nih.gov/sra/SRX5005282. These are single-end Illumina reads. Your code will
retrieve this file; i.e., you cannot just retrieve it.

For this you will need to install the SRA Toolkit to the machine you are using. You can refer to this link to guide you through the installation process, https://github.com/ncbi/sra-tools/wiki/01.-Downloading-SRA-Toolkit 

To solve this you need to format a command and use os.system to send that command to the command line 

# Problem 2. Using SPAdes, assemble the genome. Write the SPAdes command to the log file:

For this you will need to have SPADES installed on your machine.
https://cab.spbu.ru/software/spades/

This was similar approach to one where you write a command script and use os.system to send it to the command line.

# Problem 3. Calculate the number of contigs with a length > 1000 and write the # out to the log:

# Problem 4. Calculate the length of the assembly (the total number of bp in all of the contigs > 1000 bp in length) and write this # out to the log:

# Problem 5. Use GeneMarkS-2 to predict coding regions: 

You can download this software from:http://exon.gatech.edu/GeneMark/license_download.cgi. You will be given access to two gz files, one is
the code, which you should move into your home directory and unpack tar -xf filename.tar.gz. You will
also get a key. You need to gunzip filename.gz. Then copy this file to your home directory (command: cp
gm_key_64 ~/.gmhmmp2_key). (Note, this key file has to be named gmhmmp2_key and it has to be in
your home directory.) Using GeneMarkS-2, output the predicted protein sequences for the identified
genes. (If you’re doing #9, you’ll need another file too.)

# Problem 6. GeneMarkS-2 identifies coding regions but doesn’t predict what they are. 
I’ve created a multi-FASTA format file of E. coli protein sequences. (Actually, I stole it from Prokka.) Query your predicted amino
acid sequences (from #5) against these sequences to predict their function. You can find this multiFASTA format file 
at: /home/aene/Ecoli.fasta. You can copy it from her folder into yours. Query via
BLAST your predicted amino acid sequences in order to identify the predicted function of each. BLAST+
(and all its functions) are accessible to you already. In other words, you don’t have to install anything.
Produce an output file called “predicted_functionality.csv”. It should be a csv file formatted as follows:
Query sequence ID, Subject sequence ID, % Identity, % Query Coverage
Note, only report the best hit for each of your predicted sequences.

# Problem 7. The assembled genome in RefSeq for E. coli K-12 (NC_000913) has 4140 CDS and 89 tRNAs annotated.
Write to the log file the discrepancy (if any) found. For instance, if my GeneMark annotation predicted
4315 CDS, I would write, GeneMarkS found 175 additional CDS than the RefSeq.
