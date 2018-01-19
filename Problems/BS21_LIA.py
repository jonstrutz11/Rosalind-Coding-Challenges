# Rosalind - Bioinformatics Stronghold - 21 - Independent Alleles
#
# Given: Two positive integers k (k ≤ 7) and N (N ≤ 2k). In this problem,
#   we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has
#   two children in the 1st generation, each of whom has two children, and so
#   on. Each organism always mates with an organism having genotype Aa Bb.
#
# Return: The probability that at least N Aa Bb organisms will belong to the
#   k-th generation of Tom's family tree (don't count the Aa Bb mates at each
#   level). Assume that Mendel's second law holds for the factors.
#
# Updated 2/13/2017 by Jon Strutz

from math import factorial


def get_data(filename):
    with open(filename) as infile:
        data = infile.read().split()
        return int(data[0]), int(data[1])


def calc_kgen_org_num(gens):
    return 2**gens


def calc_prob_AaBb_in_k(N, org_num):
    binom = factorial(org_num)/(factorial(N) * factorial(org_num - N))
    prob = binom * .25**N * .75**(org_num - N)
    return prob


if __name__ == "__main__":
    k, N = get_data('BS21_LIA.txt')
    orgs = calc_kgen_org_num(k)
    prob_atleast_N_AaBb = 0
    for i in range(N):
        prob_atleast_N_AaBb += calc_prob_AaBb_in_k(i, orgs)
    print(1 - prob_atleast_N_AaBb)
