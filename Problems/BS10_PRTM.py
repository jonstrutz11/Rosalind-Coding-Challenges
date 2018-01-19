# Rosalind - Bioinformatics Stronghold - 10 - Calculating Protein Mass
#
# Given: A protein string P of length at most 1000 aa
#
# Return: The total weight of P. Consult the monoisotopic mass table.
#
# Updated 12/7/2016 by Jon Strutz

# Get protein string
with open('10_PRTM.txt') as inputfile:
    protein_string = inputfile.read()

# Mass of each amino acid, store in dictionary
A = 71.03711
C = 103.00919
D = 115.02694
E = 129.04259
F = 147.06841
G = 57.02146
H = 137.05891
I = 113.08406
K = 128.09496
L = 113.08406
M = 131.04049
N = 114.04293
P = 97.05276
Q = 128.05858
R = 156.10111
S = 87.03203
T = 101.04768
V = 99.06841
W = 186.07931
Y = 163.06333

aa_list = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q',
           'R', 'S', 'T', 'V', 'W', 'Y']
aa_mass_list = [A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y]

aa_mass = {}

for aa in range(0, len(aa_list)):
    aa_mass[str(aa_list[aa])] = aa_mass_list[aa]

# Calculate total mass (starting with that of a single water molecule)
total_mass = 0

for aa in protein_string:
    for eachKey in aa_mass.keys():
        if aa == eachKey:
            mass = aa_mass[eachKey]
            total_mass += mass

print(total_mass)
