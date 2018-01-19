# Rosalind - Bioinformatics Stronghold - 4 - Mendel's First Law
#
# Given: Three positive integers, k, m, and n, representing a population
#   containing k + m + n organisms: k individuals are homozygous dominant for
#   a factor, m are heterozygous, and n are homozygous recessive.
#
# Return: The probability that two randomly selected mating organisms will
#   produce an individual possessing a dominant allele (and thus displaying the
#   dominant phenotype). Assume that any two organisms can mate.
#
# Updated 12/3/2016 by Jon Strutz

with open('04_IPRB.txt') as inputfile:
    myfile = inputfile.read()

# Get k, m, n from file
numlist = [int(s) for s in myfile.split() if s.isdigit()]

k = int(numlist[0])
m = int(numlist[1])
n = int(numlist[2])
total = k + m + n

# Calculate probabilities for an organism
prob_org_k = k / total
prob_org_m = m / total
prob_org_n = n / total

total -= 1

# Calculate probabilities of each combination of organisms
kk = prob_org_k * (k - 1) / total
km = 2 * prob_org_k * m / total   # 2 from also mk
kn = 2 * prob_org_k * n / total   # also nk
mm = prob_org_m * (m - 1) / total
mn = 2 * prob_org_m * n / total   # also nm
nn = prob_org_n * (n - 1) / total

# Calculate dominance (coefficients from punnent squares)
dominance = kk + km + kn + (0.75 * mm) + (0.50 * mn) + (0 * nn)
print(dominance)
