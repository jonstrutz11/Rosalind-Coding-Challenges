# Rosalind - Bioinformatics Stronghold - 13 - Inferring mRNA from Protein
#
# Given: A protein string of length at most 1000 aa
#
# Return: The total number of different RNA strings from which the protein
# could have been translated, modulo 1,000,000. (Don't neglect the importance
# of the stop codon in protein translation.)
#
# Updated 12/14/2016 by Jon Strutz


def count_codons(sequence):
    """Counts the possible codons for amino acids of each type in the string"""
    count = 1
    STOP = 3 # 3 stop codons available
    for aa in sequence:
        if aa in ('W', 'M'):
            count *= 1
        elif aa in ('F', 'Y', 'H', 'Q', 'N', 'K', 'C', 'D', 'E'):
            count *= 2
        elif aa in ('I'):
            count *= 3
        elif aa in ('V', 'P', 'T', 'A', 'G'):
            count *= 4
        elif aa in ('L', 'S', 'R'):
            count *= 6
        else:
            print("Error: Amino acid %s not recognized." % aa)
    count *= STOP
    return count % 1000000


with open('13_MRNA.txt') as infile:
    protein_seq = infile.read()

print(count_aa(protein_seq))
