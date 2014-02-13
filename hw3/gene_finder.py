# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
import random

def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result
def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    codons = [['TTT', 'TTC'],
          ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
          ['ATT', 'ATC', 'ATA'],
          ['ATG'],
          ['GTT', 'GTC', 'GTA', 'GTG'],
          ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
          ['CCT', 'CCC', 'CCA', 'CCG'],
          ['ACT', 'ACC', 'ACA', 'ACG'],
          ['GCT', 'GCC', 'GCA', 'GCG'],
          ['TAT', 'TAC'],
          ['TAA', 'TAG', 'TGA'],
          ['CAT', 'CAC'],
          ['CAA', 'CAG'],
          ['AAT', 'AAC'],
          ['AAA', 'AAG'],
          ['GAT', 'GAC'],
          ['GAA', 'GAG'],
          ['TGT', 'TGC'],
          ['TGG'],
          ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
          ['GGT', 'GGC', 'GGA', 'GGG']]
              
    aa = ['F','L','I','M','V','S','P','T','A','Y','|','H','Q','N','K','D','E','C','W','R','G']
    sequence=''
    for i in range(len(dna)/3):
        codonstring=dna[i*3:i*3+3] #puts codns into a variable
        for n in range(len(codons)):
            if codonstring in codons[n]: #checks if codon matches wiht codon list
                sequence=sequence+str(aa[n])
    return sequence
    # YOUR IMPLEMENTATION HERE
coding_strand_to_AA('CAT')
def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    x=coding_strand_to_AA('AA')
    print 'input:', 'AA'
    print 'expected output:', ''
    print 'actual output:', x
    print ""
    x=coding_strand_to_AA('TTTTGC')
    print 'input:', 'TTT'
    print 'expected output:' ,'FC'
    print 'actual output:' , x
    print ""
    x=coding_strand_to_AA('GAGTG')
    print 'input:', 'TTT'
    print 'expected output:' ,'E'
    print 'actual output:' , x
    print ""
    # YOUR IMPLEMENTATION HERE

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    complementary=""
    for i in range(len(dna)):
        if dna[i:i+1] == 'A':
            complementary= complementary+'T'
        elif dna[i:i+1] == 'T':
            complementary= complementary+'A'
        elif dna[i:i+1] == 'C':
            complementary= complementary+'G'
        elif dna[i:i+1] == 'G':
            complementary= complementary+'C'
        else:
            complementary= complementary+'X'
    newcom=complementary[::-1] #reveses direction
    return complementary
    # YOUR IMPLEMENTATION HERE
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
    x=get_reverse_complement('aatgc')
    print 'input:', 'aatcg'
    print 'expected output:', 'ttacg'
    print 'actual output:', x
    print ""
    x=get_reverse_complement('')
    print 'input:', 'TTT'
    print 'expected output:' ,''
    print 'actual output:' , x
    print ""
    x=get_reverse_complement('ttgcwa')
    print 'input:', 'TTT'
    print 'expected output:' ,'aacgXt'
    print 'actual output:' , x
    print ""
    # YOUR IMPLEMENTATION HERE    
def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    sequence=''
    for i in range(len(dna)/3):
        A=dna[i*3:i*3+3]    
        if A=='TAG' or A=='TAA' or A=='TGA':   #checks for stop codons         
            break
        else:  #if its not a stop codon print out the codon
            sequence= sequence+A
    return    sequence         
    # YOUR IMPLEMENTATION HERE
def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
    x=rest_of_ORF('ATGG')
    print 'input:', 'ATGG'
    print 'expected output:', 'ATG'
    print 'actual output:', x
    print ""
    x=rest_of_ORF('ATGTAA')
    print 'input:', 'ATGTAA'
    print 'expected output:', 'ATG'
    print 'actual output:', x
    print ""
    x=rest_of_ORF('ATGGCAGTA')
    print 'input:', 'ATGGCAGTA'
    print 'expected output:', 'ATGGCAGTA'
    print 'actual output:', x
    print ""
    # YOUR IMPLEMENTATION HERE      
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    sequence=''
    n=0
    for i in range(len(dna)/3):
        condon=dna[i*3:i*3+3] #puts current codons into a varible
        if codon=='ATG':
            n=1     #when n=1 the sequence has started so it should print out each letter
        if codon=='TAG' or codon=='TAA' or codon=='TGA':            
            n=0     #turns off sequence
            sequence= sequence+" "    
        if n==1:
            sequence= sequence+A    
    t= sequence.split()
    return t 
    # YOUR IMPLEMENTATION HERE        
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """
    x=find_all_ORFs_oneframe('ATGTAGATGAAATAG')
    print 'input:', 'ATGTAGATGAAATAG'
    print 'expected output:', "['ATG','ATGAAA']"
    print 'actual output:', x
    print ""
    x=find_all_ORFs_oneframe('CGCATGCAGTAG')
    print 'input:', 'CGCATGCAGTAG'
    print 'expected output:', "['ATGCAG']"
    print 'actual output:', x
    print ""
    # YOUR IMPLEMENTATION HERE
def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    sequence=''
    sequence2=''
    sequence3=''
    n=0
    for i in range(len(dna)/3):
        A=dna[i*3:i*3+3] #puts first frame current codon in a varible
        if A=='ATG':
            n=1
        if A=='TAG' or A=='TAA' or A=='TGA':            
            n=0
            sequence= sequence +" "    
        if n==1:
            sequence= sequence +A    
    t= sequence.split() #makes the seqnece in to list wiht multiple elements
    n=0
    for q in range(len(dna)/3):
        A=dna[q*3+1:q*3+4] #puts second frame current codon in a varible
        if A=='ATG':
            n=1
        if A=='TAG' or A=='TAA' or A=='TGA':            
            n=0
            sequence2= sequence2 +" "    
        if n==1:
            sequence2= sequence2 +A    
    y= sequence2.split()
    n=0
    for w in range(len(dna)/3):
        A=dna[w*3+2:w*3+5] #puts last frame current codon in a varible
        if A=='ATG':
            n=1
        if A=='TAG' or A=='TAA' or A=='TGA':            
            n=0
            sequence3= sequence3 +" "    
        if n==1:
            sequence3= sequence3 +A    
    u= sequence3.split() 
    B=[t,y,u]
    return B
    # YOUR IMPLEMENTATION HERE

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
    x=find_all_ORFs('ATGAATGCATGC')
    print 'input:', 'ATGTAGATGAAATAG'
    print 'expected output:', "[['ATGAATGCATGC'], ['ATGCATGC'], ['ATGC']]"
    print 'actual output:', x
    print ""
    x=find_all_ORFs('ATGTAAATG')
    print 'input:', 'ATGTAAATG'
    print 'expected output:', "[['ATG', 'ATG'], [], []]"
    print 'actual output:', x
    print "" 
    # YOUR IMPLEMENTATION HERE
def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    reversecom=get_reverse_complement(str(dna))
    B1=find_all_ORFs(str(dna)) #original strand
    B2=find_all_ORFs(str(reversecom)) #revese com strad
    answer=[B1,B2]   
    return answer
    # YOUR IMPLEMENTATION HERE

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """
    x=find_all_ORFs_both_strands('ATGCGAATGTAGCATCAAA')
    print 'input:', 'ATGTAGATGAAATAG'
    print 'expected output:', "['ATGCGAATG ', ' ATGCTACATTCGCAT']"
    print 'actual output:', x
    print ""
    x=find_all_ORFs_both_strands('GATGCGATTAATAGATG')
    print 'input:', 'GATGCGATTAATAGATG'
    print 'expected output:', "[[[], ['ATGCGATTAATAGAT'], ['ATG']], [[], [], []]]"
    print 'actual output:', x
    print ""
    # YOUR IMPLEMENTATION HERE
def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""
    ListORF= find_all_ORFs_both_strands(str(dna))
    flattenList=flatten(ListORF) #gets rid of all nested lists
    if len(flattenList)== 0: #prevents an error when using max()
        return ''
    else:
        return max(flattenList, key=len) #returns longest element in in flatten lists
    # YOUR IMPLEMENTATION HERE
def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """
    x=longest_ORF('ATGCGAATGTAGCATCAAA')
    print 'input:', 'ATGCGAATGTAGCATCAAA'
    print 'expected output:', "ATGCTACATTCGCAT"
    print 'actual output:', x
    print ""
    x=longest_ORF('ATGAATGATAGTAATATG')
    print 'input:', 'ATGAATGATAGTAATATG'
    print 'expected output:', "ATGAATGATAGTAATATG"
    print 'actual output:', x
    print ""
    # YOUR IMPLEMENTATION HERE
def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    dnalist=list(str(dna))  
    L=[]      
    for i in range(num_trials): #loops for num of trials
        random.shuffle(dnalist) 
        randomstring = collapse(dnalist) #makes random lsits into a string
        longestString=longest_ORF(str(randomstring))
        L.append(str(longestString))

    if len(L) == 0: #prevents error when lsit is blank
        return ""
    else:
        return max(L, key=len)
from load import load_seq
dna = load_seq("data/X73525.fa")        
       
    # YOUR IMPLEMENTATION HERE
def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified."""
    codons = [['TTT', 'TTC'],
          ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
          ['ATT', 'ATC', 'ATA'],
          ['ATG'],
          ['GTT', 'GTC', 'GTA', 'GTG'],
          ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
          ['CCT', 'CCC', 'CCA', 'CCG'],
          ['ACT', 'ACC', 'ACA', 'ACG'],
          ['GCT', 'GCC', 'GCA', 'GCG'],
          ['TAT', 'TAC'],
          ['TAA', 'TAG', 'TGA'],
          ['CAT', 'CAC'],
          ['CAA', 'CAG'],
          ['AAT', 'AAC'],
          ['AAA', 'AAG'],
          ['GAT', 'GAC'],
          ['GAA', 'GAG'],
          ['TGT', 'TGC'],
          ['TGG'],
          ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
          ['GGT', 'GGC', 'GGA', 'GGG']]
              
    aa = ['F','L','I','M','V','S','P','T','A','Y','|','H','Q','N','K','D','E','C','W','R','G']
    finalaalist=[]
    Openframes=find_all_ORFs(str(dna))
    flattenOpenframes=flatten(Openframes)
    for i in range(len(flattenOpenframes)):
        if len(flattenOpenframes[i])>int(threshold):
            strand=flattenOpenframes[i]
            aa= coding_strand_to_AA(strand)
            finalaalist.append(str(aa))
          
    return finalaalist
    # YOUR IMPLEMENTATION HERE
