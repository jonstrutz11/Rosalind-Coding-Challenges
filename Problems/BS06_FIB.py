# Rosalind - Bioinformatics Stronghold - 6 - Rabbits and Recurrence Relations
#
# Given: Positive integers n <= 40 and k <= 5
#
# Return: The total number of rabbit pairs that will be present after n months,
#   if we begin with 1 pair and in each generation, every pair of
#   reproduction-age rabbits produces a litter of k rabbit pairs (instead of
#   only 1 pair).
#
# Updated 12/5/2016 by Jon Strutz

# Get n and k from file
with open('06_FIB.txt') as inputfile:
    s = inputfile.read()
    numlist = [int(s) for s in s.split()]

n = numlist[0]
k = numlist[1]

# Initialize F_n-1 and F_n-2
f_1 = 1
f_2 = 1


# Calculate F_n
for i in range(n):
    if i > 1:
        f = f_1 + k * f_2
        f_2 = f_1
        f_1 = f
    else:
        f = 1

# Print result
print(f)
