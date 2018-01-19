# Example: Finding a Motif in DNA
# Jon Strutz - 1/24/2017
#
# Given: Two DNA strings s and t (each of length at most 1 kbp).
#
# Return: All locations of t as a substring of s.


import sys


buffer = []
line_num = 0
run = True
while run:
    line = sys.stdin.readline().rstrip('\n')
    line_num += 1
    if line_num >= 2:
        run = False
    buffer.append(line)


s, t = buffer

sub_len = len(t)
seq_len = len(s)

locations = []

for base_num in range(len(s)):
    if base_num <= seq_len - sub_len + 1:
        if s[base_num : base_num + sub_len] == t:
            locations.append(str(base_num + 1))

print(" ".join(locations))

