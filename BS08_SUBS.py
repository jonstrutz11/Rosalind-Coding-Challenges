# Rosalind - Bioinformatics Stronghold - 8 - Finding a Motif in DNA
#
# Given: Two DNA Strings s and t (each of length at most 1 kbp).
#
# Return: All locations of t as a substring of s.
#
# Updated 12/5/2016 by Jon Strutz

# Get s and t from dataset
with open('08_SUBS.txt') as inputfile:
    sequences = inputfile.read()

s, t = sequences.split()

# Initialize location data
locations = []

# Find locations of t in s and append to locations list
for base_num in range(0, len(s) + 1):
    if s[base_num : base_num + len(t)] == t:
        locations.append(str(base_num + 1))

# Print all locations on one line separated by a space
print(' '.join(locations))
