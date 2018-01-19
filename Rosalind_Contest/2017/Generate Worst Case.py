# Generate 10^5/2 (50000) chemical reactions with one reactant and one product
#   each
# Updated 1/28/17 by Jon Strutz


prob_reactant2 = 0
prob_product2 = 0

with open('Chemical Reactions Input File (Hard).txt', 'w') as outfile:
    outfile.write('1' + '\n')
    i = 50000
    while i > 1:
        reactant1 = str(i-1)
        product1 = str(i)
        i -= 1
        reaction = reactant1 + '->' + product1 + '\n'
        outfile.write(reaction)