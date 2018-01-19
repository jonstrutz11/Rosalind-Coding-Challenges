# Rosalind Bioinformatics Contest - Qualifying Round
# Problem 1 - Chemical Reactions (Easy)
# Jon Strutz - 1/24/2017

import sys


# Get data as a list
buffer = sys.stdin.readlines()

for line_num in range(len(buffer)):
    buffer[line_num] = buffer[line_num].rstrip('\n')


# Get initial reactants from first line of list and reactions list from rest
initial_reactants = buffer.pop(0).split(' ')
reactions_list = buffer


# Convert list of reactions to dictionary of reactants and products
reactions_dict = {}
for reaction in reactions_list:
    if '->' in reaction:
        reactants, products = reaction.split('->')

    # If multiple reactants or products, replace + with a space
    if '+' in reactants:
        reactants = reactants.split('+')
    if '+' in products:
        products = products.split('+')

    # Can't have a reaction like 1->1+2
    if len(products) == 2 and len(reactants) == 1 and reactants in products:
        continue

    if isinstance(reactants, list):
        reactants = "+".join(reactants)
    if isinstance(products, list):
        products = "+".join(products)

    # If reactants key already exists in dictionary, then add the new product
    #  to that key's value
    if reactants not in reactions_dict:
        reactions_dict[reactants] = products
    elif reactants in reactions_dict:
        reactions_dict[reactants] += ('+' + products)
    else:
        print("Error: could not move all reactions in list to dictionary.")

# Find all possible products
possible_products = initial_reactants
reaction_possible = True
current_reactants = None
while reaction_possible is True:

    # Check if reaction is possible
    for reactants in reactions_dict:
        reactants = reactants.split('+')
        if len(reactants) > 1:
            reactant1 = reactants[0]
            reactant2 = reactants[1]
            if reactant1 and reactant2 in possible_products:
                current_reactants = reactants
        else:
            reactant1 = reactants
            if reactant1 in possible_products:
                current_reactants = reactant1

    if current_reactants is None:
        reaction_possible = False

    # Do reaction
    if reaction_possible is True:
        products = reactions_dict[current_reactants].split('+')
        for product in products:
            if product not in possible_products:
                possible_products.append(product)
        # Delete reaction
        reactions_dict.pop(current_reactants)

    current_reactants = None
    reactant1 = None
    reactant2 = None

print(' '.join(possible_products))
