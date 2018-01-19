# Rosalind - Bioinformatics Stronghold - 12 - Calculating Expected Offspring
#
# Given: Six positive integers, each of which does not exceed 20,000. The
#   integers correspond to the number of couples in a population possessing each
#   genotype pairing for a given factor. In order, the six given integers
#   represent the number of couples having the following genotypes:
#   1. AA-AA
#   2. AA-Aa
#   3. AA-aa
#   4. Aa-Aa
#   5. Aa-aa
#   6. aa-aa
#
# Return: The expected number of offspring displaying the dominant phenotype in
#   the next generation, under the assumption that every couple has exactly two
#   offspring.
#
# Updated 12/14/2016 by Jon Strutz

# Get data from file
with open('12_IEV.txt') as infile:
    data = infile.read()
    numlist = [int(s) for s in data.split()]

nAA_AA = numlist[0]
nAA_Aa = numlist[1]
nAA_aa = numlist[2]
nAa_Aa = numlist[3]
nAa_aa = numlist[4]
naa_aa = numlist[5]

# Calculate expected offspring
expected_offspring = 2 * (nAA_AA + nAA_Aa + nAA_aa + 0.75 * nAa_Aa +
                          0.5 * nAa_aa)

print(expected_offspring)