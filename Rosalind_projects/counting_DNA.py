#Python script to count the nucleotides within a DNA string sequence 

def count_DNA(s):
    A = 0 
    G = 0
    C = 0
    T = 0

    for nucleotide in s:
        if nucleotide == 'A':
            A = A+1
        elif nucleotide =='G':
            G = G+1 
        elif nucleotide == 'C':
            C = C+1 
        elif nucleotide == 'T':
            T = T+1 
    
    print(A)
    print(C)
    print(G)
    print(T)

string = 'CTAGAGTTAGTTCATTGCGCTACAACTAGGTTGAGATTGGTTTCGGGCATTGTGGGCGACAAGACTAATACGGATCCATGTCTGGCCTCACCTCTCCTTGATCTTGCACGATATAGCGGTGCTTCGTATGACTAGCCCTCAAAAGGATGAGCAAGCCATGCGTCGGAGCATATTTCAACACGTCTATACGTGCAGACAAATCGGTAACACATAGCGCGAGCAGTGAGCCTCCAACTGCACGGAATCTTGAATGGGCAAGTGTGCAAACACAACGAGGAGCTAAATCCTCGAGGGGCCGCTTGGGCCATTCCCTAAGTTCATGTGTTCCGAAACCGTCACTATTTATTAGACTCCGCAAGACATCTCCAAAATAGTAACCGACGAACTCGGTTCACTGCTCGTCGTTGTCGACTACCAATGGCCTTTATCTGCTTCTCCAGTTTGCTAACCTATCCTTACTACCTGATCAAGCATGGCAACAGGGGGACCTCTGGGCGAACATACAGCAGATGTTGATTCGTATGGGACGAATGTAGGGCGTTGCCCGATCAGCGTCGGAATTTCTCCGACCATTTGATTCAAGAAGAGGTGTGGTAAGCCCTTGCTTGCTGCTGAAGGAGGAGCCTATCCTATTATGAGCTAGAAGTTCGCGAGGCCAGCCAGTAGTATCTTGCGAATGGATATCATCGTGGCCCTGGAACCGGCAGCAGGTAGATGACAGACCGTCACGGCAGTACCCATGAACTGGCCTGTGATCTGGTCGGGGAGGGTTCATAATGGCGTGACCGTTCGACAGATCTTGTCCTTTCATAGAACATGGCCGCTCAGCACTAATATTTACCCTAGAACAAGCGAAAAAACTCTCTACTACCCCTGAGTTGCGATGTGCTCGGTGCGTGCCCATTTAAACAACGGCGTAGCATCAGTGTGGGGGATAGCGTAGCACGCGCGGCTGCCGTGAAAAATGTTGATGACGTCAGATGAGGCTTTGGGCT'

count_DNA(string)