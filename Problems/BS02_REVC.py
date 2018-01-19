# Rosalind - Bioinformatics Stronghold - 2 - The Secondary and Tertiary
#                                            Structures of DNA
#
# Given: A DNA string s of length at most 1000 bp.
#
# Return: The reverse complement sc of s.

with open("rosalind_revc.txt", 'r') as myfile:
    s = myfile.read()

slist = list(s)

for i in range(len(slist)):
    if slist[i] == 'A':
        slist[i] = 'T'
    elif slist[i] == 'C':
        slist[i] = 'G'
    elif slist[i] == 'G':
        slist[i] = 'C'
    elif slist[i] == 'T':
        slist[i] = 'A'

slist.reverse()

sc = "".join(slist)
print(sc)
