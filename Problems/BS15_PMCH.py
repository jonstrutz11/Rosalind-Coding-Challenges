# Rosalind - Bioinformatics Stronghold - 15 - Perfect Matchings and RNA
#                                             Secondary Structures
#
# Given: An RNA string s of length at most 80 bp having the same number of
#   occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.
#
# Return:  The total possible number of perfect matchings of basepair edges in
#   the bonding graph of s.
#
# Updated 12/21/2016 by Jon Strutz


def count_nuc(RNAstring):
    au_count = RNAstring.count('A') # same number of a as u
    cg_count = RNAstring.count('C') # same number of c as g
    return au_count, cg_count


def total_matchings(au, cg):
    i = au
    j = cg
    au_matchings = au
    cg_matchings = cg

    while i > 1:
        au_matchings *= i - 1
        i -= 1

    while j > 1:
        cg_matchings *= j - 1
        j -= 1

    total = au_matchings * cg_matchings
    return total


# Main code
with open('15_PMCH.txt') as infile:
    s = infile.read()


RNAstring = ''
for character in s:
    if character in ('A', 'C', 'G', 'U'):
        RNAstring += character

au_count, cg_count = count_nuc(s)

print(total_matchings(au_count, cg_count))