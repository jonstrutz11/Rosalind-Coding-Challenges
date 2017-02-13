# Rosalind - Bioinformatics Stronghold - 16 - Finding a Shared Motif
#
# Given: A collection of k (k <= 100) DNA strings of length at most 1 kbp each
#   in FASTA format.
#
# Return: A longest common substring of the collection. (If multiple solutions
#   exist, you may return any single solution.)
#
# Updated 12/27/2016 by Jon Strutz

ids = []
seqs = []
seq = ''
seq_dict = {}

with open('16_LCSM.txt') as infile:
    k = infile.read().count('>')

with open('16_LCSM.txt') as infile:
    for line in infile:
        line = line.strip()

        if '>' in line:
            ids.append(line)

            if not line == '>Rosalind_1\n':
                seqs.append(seq)
                seq = ''

        else:
            seq += line

    seqs.append(seq)
    seqs.pop(0)


def long_substr(seqs):
    substr = ''
    if len(seqs) > 1 and len(seqs[0]) > 0:
        for i in range(len(seqs[0])):
            for j in range(len(seqs[0])-i+1):
                if j > len(substr) and is_substr(seqs[0][i:i+j], seqs):
                    substr = seqs[0][i:i+j]
    return substr


def is_substr(find, seqs):
    if len(seqs) < 1 and len(find) < 1:
        return False
    for i in range(len(seqs)):
        if find not in seqs[i]:
            return False
    return True

print(long_substr(seqs))



