# Rosalind - Bioinformatics Stronghold - 26 - Introduction to Random Strings
#
# Given: A DNA string s of length at most 100 bp and an array A containing at
#  most 20 numbers between 0 and 1.
#
# Return: An array B having the same length as A in which B[k] represents the
#  common logarithm of the probability that a random string constructed with
#  the GC-content found in A[k] will match s exactly.
#
# Updated 4/27/2017 by Jon Strutz

from math import log10


def get_data(filename):
    with open(filename, "r") as infile:
        dna_string = infile.readline().strip()
        gcArray = infile.readline().split(' ')
    return dna_string, gcArray


def get_dna_probability(dna_string, GClist):
    dna_probability = [1 for i in GClist]
    for index, GC_probability in enumerate(GClist):
        for base in dna_string:
            if base == "C" or base == "G":
                dna_probability[index] *= float(GC_probability) / 2
            elif base == "A" or base == "T":
                dna_probability[index] *= (1 - float(GC_probability)) / 2
            else:
                raise ValueError("Base not recognized. Must be A, C, G, or T.")
    for index, value in enumerate(dna_probability):
        dna_probability[index] = log10(value)
    return dna_probability


def write_outfile(filename, list):
    with open(filename, "w") as outfile:
        for probability_value in list:
            outfile.write(str(round(probability_value, 3)) + " ")


if __name__ == "__main__":
    s, A = get_data("BS26_PROB.txt")
    B = get_dna_probability(s, A)
    write_outfile("BS26_PROB_out.txt", B)