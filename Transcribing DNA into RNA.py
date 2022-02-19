# Problem: Transcribing DNA into RNA from ROSALIND
# Author: Steven Sommer
# Date: 2/18/2022

def count_bases1(s):
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0

    for b in s: # not {
        if b == 'A': # indentation used for code block
            a_count += 1
        if b == 'C':
            c_count += 1
        if b == 'G':
            g_count += 1
        if b == 'T':
            t_count += 1
    
    print('A = ', a_count)
    print('C = ', c_count)
    print('G = ', g_count)
    print('T = ', t_count)
    print()
    print(a_count, c_count, g_count, t_count) # not println
    return

def count_bases2(s):
    aa_count = s.count('A')
    cc_count = s.count('C')
    gg_count = s.count('G')
    tt_count = s.count('T')

    print(aa_count, cc_count, gg_count, tt_count)
    return

def count_bases3(s):
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0
    
    for i in range(len(s)): # 0 .. len(s)-1
        if s[i] == 'A': # indentation used for code block
            a_count += 1
        if s[i] == 'C':
            c_count += 1
        if s[i] == 'G':
            g_count += 1
        if s[i] == 'T':
            t_count += 1
        
    print(a_count, c_count, g_count, t_count) # not println
    return


def transcription(s):
    rna = s.replace('T', 'U')
    print(rna)
    return

def transcription2(s):
    rna = ' '
    for i in range(len(s)):
        if s[i] == 'T':
            rna += 'U' # concatenation
        else:
            rna += s[i]
    print(rna)
    return

s = 'CCCGGGAAAGTCAACAGTCGTTGTAATTGCCTTATAGAGTCTCAAGCAAACCAGTGTCGAACCCTCAGAGACTGTGGCTATCAATGAGCCGAAGAGGGAGGCAGATTCAGAGAAATTGCTAGGCCCCTGTACCGGCCGACTGCTTCCCTGAATATCCAATATATTACCTCAGAAATGTTTCTTATTAGGTCTATTCAGACGCTGTACACCTGAACAGGCTCCTGGTGAACCGTTATAATGGCTAGTATCAACTGCGCTAGGGTCAGTAGTTCCCACCGAGCAGAAGCTCTACACTGACACTACCTTTGAACAAACTGGCCCACAACCATTGCGCCGTGTTCAAAGAGTCATCGGTACCTGTGAAACAAGCCGCGGTAGCATAGCGCGATATCCAGGCTCCGTCTACGGTGAGTGTTGATAGACGTCCACCTGACGCTATCTTTTTCTGGTAGGATACCTTCGGACCATTCAGCTATCGTGCTTTTCGGCCCCTCACCCTACCTGGAACTATGTGGTGAAGATCTGCAGTTGTCCTAACGAGAGAACTGATCAGTGTCCAGGTTTGCATGAATGACATATTCTTCCCGAGAATATCAGGCAATCCCGAGATCAAGACGCCTCAACTCCGTTTGACCATCTGTAATCTTTCCGTATTACGGTTCTATCAGACCAATGTGAGCACAATTTTCGCGGTTCTAATCCGGCACCTCTTCGGGCAGAGCGGCCGAAGCCTCGCTCTGCGCTATTTTGGTTCTGCCGTATCTTATTTTAAAAGTCGCAAACGATGAAGTAACACCGATGTTGGAGAATCAGTATTGCGCCAGCGTGCGAGAACTCTCAATTTTCCAAGCCGTTCTCAAAAGTTCCTTTGTTCACGGCTTGCGGCGATCGAGCGTTAACGAATCCATTCGTGACTTATTCGTATGACGAGGCCGCATCACCGGTTAGTGCTCGAATAATACGTTTTACTAACGCAGGTACTATTCTTTTGGCAATT' # no ;
count_bases1(s)
count_bases2(s)
count_bases3(s)
transcription(s)
