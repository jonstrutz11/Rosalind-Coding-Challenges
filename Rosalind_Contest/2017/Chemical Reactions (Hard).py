# Rosalind Bioinformatics Contest - Qualifying Round
# Problem 1 - Chemical Reactions (Hard)
# Jon Strutz - 1/28/2017

import sys
import bisect


with open('Chemical Reactions Input File (Hard).txt') as infile:
    sys.stdin = infile
    initial_reactants = sys.stdin.readline().split()
    buffer = sys.stdin.readlines()

# Get data as a list
# initial_reactants = sys.stdin.readline().split()
# buffer = sys.stdin.readlines()

for line_num in range(len(buffer)):
    buffer[line_num] = buffer[line_num].rstrip('\n')

# buffer = set()
#
# with open('Chemical Reactions Input File (Hard).txt') as infile:
#     initial_reactants = infile.readline().rstrip('\n')
#     for line in infile:
#         buffer.add(line.rstrip('\n'))

# # Get initial reactants from first line of list and reactions list from rest
# initial_reactants = set(initial_reactants.split(' '))
reactions_list = set(buffer)
same = []
# Convert list of reactions to dictionary of reactants and products
reactions_dict = {}
reactants = None
products = None
for reaction in reactions_list:
    reverse_reactants = None

    if '->' in reaction:
        reactants, products = reaction.split('->')

    if reactants == products:
        same.append(reactants)

    unreal1_possible = 1
    unreal2_possible = 0
    if '+' in reactants:
        reactants = reactants.split('+')
        unreal1_possible = 0
    if '+' in products:
        products = products.split('+')
        unreal2_possible = 1
    # Can't have a reaction like 1->1+2
    # print('   ', reactants, products)
    # print('   ', unreal1_possible, unreal2_possible)
    # print(reactants, products)
    if unreal1_possible and unreal2_possible and reactants in products:
            continue

    if unreal2_possible:
        if products[0] == products[1]:
            continue

    if isinstance(reactants, list):
        reactants = '+'.join(reactants)
    if isinstance(products, list):
        products = '+'.join(products)

    # If reactants key already exists in dictionary, then add the new product
    #  to that key's value
    if '+' in reactants:
        reactant12 = reactants.split('+')
        reverse_reactants = str(reactant12[1]) + '+' + str(reactant12[0])
    if reverse_reactants and reverse_reactants in reactions_dict:
        reactions_dict[reverse_reactants] += ('+' + products)
    elif reactants not in reactions_dict:
        reactions_dict[reactants] = products
    elif reactants in reactions_dict:
        reactions_dict[reactants] += ('+' + products)
    else:
        print("Error: could not move all reactions in list to dictionary.")

# print('reactions:', reactions_dict)
reactant1_list = []
reactant2_dict = {}

# Get list of all reactants (in order)
for reaction in reactions_dict:
    if '+' not in reaction:
        reactant1_list.append(int(reaction))
        reactant2_dict[reaction] = []
    else:
        reaction = reaction.split('+')
        for reactant in reaction:
            reactant2_dict[reactant] = []
# print(reactant1_list)
# print(reactant2_dict)
for reaction in reactions_dict:
    if len(reaction.split('+')) == 2:
        reactant1, reactant2 = reaction.split('+')
        reactant2_dict[reactant1].append(reactant2)
        reactant2_dict[reactant2].append(reactant1)

for reaction in same:
    reactant2_dict[reaction] = []
#
# print('reactant2_dict:', reactant2_dict)
reactant1_list = list(set(reactant1_list))
reactant1_list = sorted(reactant1_list)
# print('reaction1_list', reactant1_list)

# Find all possible products
stack = initial_reactants
possible_products = set(stack)

current_reactants = None
current_reactants2 = None
old_reactants = []
all_reactions_fulfilled = False
reactant2 = None
while stack:

    reaction1_possible = False
    reaction2_possible = False
    # Check if reaction is possible
    # print('stack:', stack)
    if all_reactions_fulfilled:
        if not stack:
            break
        elif len(stack) > 1:
            reactant1 = int(stack[-1])
        else:
            reactant1 = int(stack[0])
        all_reactions_fulfilled = False
        # print('reactant1a: ', reactant1)
        stack.pop()
    elif len(stack) > 0:
        reactant1 = int(stack[-1])
        # print('reactant1: ', reactant1)

    try:
        reactant2_dict[str(reactant1)]
    except:
        reactant2_dict[str(reactant1)] = []

    index = bisect.bisect(reactant1_list, reactant1)
    # print('index', index)
    # print(reactant1_list)

    if len(reactant1_list) > 0:
        if index == 0:
            if reactant1 == reactant1_list[index]:
                current_reactants = reactant1
                reaction1_possible = True

            for reactant in stack:
                if str(reactant) in reactant2_dict[str(reactant1)] and \
                        str(reactant1) != str(reactant):
                    key = str(reactant1) + '+' + str(reactant)
                    key2 = str(reactant) + '+' + str(reactant1)
                    current_reactants = str(key)
                    current_reactants2 = str(key2)
                    reaction2_possible = True
                    reactant2 = reactant
                    # print('reaction2_possible')
                    break

        elif index > 0:
            if reactant1 == reactant1_list[index - 1]:
                current_reactants = reactant1
                reaction1_possible = True

            for reactant in stack:
                if str(reactant) in reactant2_dict[str(reactant1)] and \
                        str(reactant1) != str(reactant):
                    key = str(reactant1) + '+' + str(reactant)
                    key2 = str(reactant) + '+' + str(reactant1)
                    current_reactants = str(key)
                    current_reactants2 = str(key2)
                    reaction2_possible = True
                    reactant2 = reactant
                    # print('reaction2_possible')
                    break

    # print('reactant1:', reactant1)
    # print('reactant2:', reactant2)
    # print('current1', current_reactants)
    # print('current2', current_reactants2)
    # Do reaction
    if reaction1_possible or reaction2_possible:
        try:
            products = reactions_dict[str(current_reactants)].split('+')
        except:
            current_reactants = current_reactants2
            products = reactions_dict[str(current_reactants)].split('+')
        for product in products:
            if product not in stack:
                stack.append(product)
                possible_products.add(product)
            if current_reactants2:
                try:
                    products2 = reactions_dict[str(current_reactants2)].split('+')
                except:
                    break
                for product in products2:
                    if product not in stack:
                        stack.append(product)
                        possible_products.add(product)

        # Delete reaction
        try:
            reactions_dict.pop(str(current_reactants))
        except:
            reactions_dict.pop(str(current_reactants2))

    all_reactions_fulfilled = True

    if reaction2_possible:
        reactant2_partners = reactant2_dict[str(reactant1)]
        # print('partners', reactant2_partners)
        if reactant2_partners:
            reactant2_dict[str(reactant1)].remove(str(reactant2))
            all_reactions_fulfilled = False
            # print('all reactions not fulfilled')
    # print('re2dict', reactant2_dict)
    # print(reaction2_possible, reactant2)
    elif isinstance(current_reactants, int):
        reactant1_list.remove(reactant1)
    current_reactants = None
    current_reactants2 = None

print(' '.join(possible_products))
# print(len(possible_products))