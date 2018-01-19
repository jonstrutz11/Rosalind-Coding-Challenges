# Rosalind - Bioinformatics Stronghold - 23 - Enumerating Gene Orders
#
# Given: A positive integer n <= 7.
#
# Return: The total number of permutations of length n, followed by a list of
#  all such permutations (in any order)
#
# Updated 3/24/2017 by Jon Strutz

import sys
from math import factorial
from itertools import permutations

n = int(sys.argv[1])

num_permutations = factorial(n)

perm_iterator = permutations(range(1, n + 1))

with open('BS23_PERM.txt', 'w') as outfile:
    outfile.write(str(num_permutations) + '\n')
    for perm_num in range(num_permutations):
        perm = next(perm_iterator)
        for value in perm:
            outfile.write(str(value) + ' ')
        outfile.write('\n')
