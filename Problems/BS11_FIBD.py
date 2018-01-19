# Rosalind - Bioinformatics Stronghold - 11 - Mortal Fibonacci Rabbits
#
# Given: Positive integers n <= 100 and m <= 20.
#
# Return: The total number of pairs of rabbits that will remain after the n-th
#   month if all rabbits live for m months.
#
# Updated 12/7/2016 by Jon Strutz

# Get n and m from file
with open('11_FIBD.txt') as inputfile:
    s = inputfile.read()
    numlist = [int(s) for s in s.split()]

n = numlist[0]
m = numlist[1]

# Initialize tracking variables
age_counts = {}
for age in range(0, m):
    age_counts[age] = 0

age_counts[0] = 1

# Go through each month
for month_num in range(n):

    # Calculate new f
    f = 0
    for j in range(m):
        f += age_counts[j]

    # Get new values for age_counts based on previous age_count values
    old_age = dict(age_counts)
    age_counts[0] = 0
    for j in range(1, m):
        age_counts[0] += old_age[j]
    for j in range(1, m):
        age_counts[j] = old_age[j - 1]

# Print result
print(f)
