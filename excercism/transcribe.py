'''
Given a DNA strand, return its RNA complement (per RNA transcription).

Both DNA and RNA strands are a sequence of nucleotides.

The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).

The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).

Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:

G -> C
C -> G
T -> A
A -> U
'''

def transcribe_rna(dna_strand):
    #decryption refrence
    nucleotionary = {
    'G':'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
    }
    rna_strand = ''
    for nucleotide in dna_strand:
        rna_strand+=nucleotionary[nucleotide]
    return rna_strand

dna_strand = 'AGCTCGACCAAACGTTTGGTTAATTCGA'
print(transcribe_rna(dna_strand))
