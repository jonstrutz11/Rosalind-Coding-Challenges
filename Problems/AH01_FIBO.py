# Rosalind - Algorithmic Heights - Fibonacci Numbers
#
# Given: A positive integer n <= 25.
#
# Return: The value of Fn
#
# Updated 02/16/2017 by Jon Strutz

with open('AH01_FIBO.txt') as infile:
    n = int(infile.read().rstrip('\n'))

i1 = 0
i2 = 1
for i in range(1, n):
    i3 = i1 + i2
    i1 = i2
    i2 = i3

print(i2)
