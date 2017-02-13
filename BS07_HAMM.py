# Rosalind - Bioinformatics Stronghold - 7 - Counting Point MUtations
#
# Given: Two DNA Strings s and t of equal length (not exceeding 1 kbp)
#
# Return: The Hamming distance dH(s,t).
#
# Updated 12/5/2016 by Jon Strutz

# Get s and t from file
with open('07_HAMM.txt') as inputfile:
    sequences = inputfile.read()

s, t = sequences.split()

# Initialize Hamming distance variable
dH = 0

# Calculate Hamming distance
for base_num in range(len(s)):
    if s[base_num] != t[base_num]:
        dH += 1

# Output Hamming distance
print(dH)
