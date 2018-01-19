# Rosalind - Bioinformatics Stronghold - 3 - Transcribing DNA into RNA
#
# Given: A DNA string t having length at most 1000 nt.
#
# Return: The transcribed RNA string of t.

with open('rosalind_rna.txt', 'r') as inputfile:
    t = inputfile.read()

rna = list(t)

for i in range(0,len(rna)):
    if rna[i] == 'T':
        rna[i] = 'U'

rna = "".join(rna)

print(t)
print(rna)
