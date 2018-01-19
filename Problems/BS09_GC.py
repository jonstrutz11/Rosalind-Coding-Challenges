# Rosalind - Bioinformatics Stronghold - 9 - Computing GC Content
#
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
#
# Return: The ID of the string having the highest GC-content, followed by the
#   GC-content of that string. Rosalind allows for a default error of 0.001 in
#   all decimal answers unless otherwise stated; please see the note on absolute
#   error below.
#
# Updated 12/6/2016 by Jon Strutz

# Use numpy for finding max value from a list later
import numpy as np

# Get data from dataset
with open('09_GC.txt') as inputfile:
    s = inputfile.read()

# Initialize variables
ids = []
sequences = []
current_sequence = ''
GC_count = 0
GC_content = []

# Create a list of ids and a list of sequences with same indices
for i in range(0, len(s)):
    if s[i] == '>':
        ids.append(str(s[(i + 1):(i + 14)]))
        if s[i + 14] == '\n':
            j = i
            while s[j + 14] != '>':
                current_sequence += s[j + 14]
                if j + 15 < len(s):
                    j += 1
                else:
                    break
        seq_string = ''.join(current_sequence)
        current_sequence = ''
        if seq_string not in sequences:
            sequences.append(seq_string)

# Calculate GC Content of each sequence
for i in range(0, len(sequences)):
    for j in range(0, len(sequences[i])):
        if sequences[i][j] == 'G' or sequences[i][j] == 'C':
            GC_count += 1
    GC_content.append(GC_count / (len(sequences[i]) - sequences[i].count('\n')))
    GC_count = 0

# Print id and GC content of highest
index_max = np.argmax(GC_content)
print(ids[index_max])
print(100 * GC_content[index_max])
