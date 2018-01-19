# Generate 10^5/2 (50000) chemical reactions with one reactant and one product
#   each
# Updated 1/28/17 by Jon Strutz


import random

prob_reactant2 = 0.5
prob_product2 = 0.5

with open('Chemical Reactions Input File (Hard).txt', 'w') as outfile:
    outfile.write('1 2 3 4' + '\n')
    i = 0
    while i < 100000:
        if random.random() < prob_reactant2:
            reactant2 = '+' + str(random.randint(1, 1000))
            i += 1
        else:
            reactant2 = ''
        if random.random() < prob_product2:
            product2 = '+' + str(random.randint(1, 1000))
            i += 1
        else:
            product2 = ''
        reactant1 = str(random.randint(1, 1000))
        product1 = str(random.randint(1, 1000))
        i += 2
        reaction = reactant1 + reactant2 + '->' + product1 + product2 + '\n'
        outfile.write(reaction)

