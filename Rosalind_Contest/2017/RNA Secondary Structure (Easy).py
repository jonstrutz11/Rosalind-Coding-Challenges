# Rosalind Bioinformatics Contest
# Problem 2 - RNA Secondary Structure
# Updated 1/29/2017 by Jon Strutz

import sys

# with open('RNA Test.txt') as infile:
#     sys.stdin = infile
#     RNA_string = sys.stdin.readline().rstrip('\n')

RNA_string = sys.stdin.readline().rstrip('\n')


# Figure out if even or odd string
def even_or_odd(rna_seq):
    if len(rna_seq) % 2 == 0:
        return 'even'
    else:
        return 'odd'


# Make a bond between two bases
def bond_possible(base1, base2):
    if base1 == base2:
        return False
    else:
        if base1 == 'A' and base2 == 'U':
            return True
        elif base1 == 'U' and base2 == 'A':
            return True
        elif base1 == 'C' and base2 == 'G':
            return True
        elif base1 == 'G' and base2 == 'C':
            return True
        else:
            return False


def delve(rna_seq, bond_list):
    for base_num in range(1, len(rna_seq)):
        if not bond_list[base_num - 1]:
            base1 = rna_seq[base_num - 1]
            base3 = rna_seq[base_num]
            if bond_possible(base1, base3):
                bond_list[base_num - 1] = 1
                bond_list[base_num] = 1
    new_seq = ''
    for index in range(len(bond_list)):
        if bond_list[index] == 0:
            new_seq += str(rna_seq[index])
    # print('new', new_seq)
    new_bond_list = [0] * len(new_seq)

    if new_seq == '':
        return True
    elif new_bond_list != bond_list:
        return delve(new_seq, new_bond_list)
    else:
        return False


# If even, check if perfect
def check_perfect(rna_seq):
    case_test_output = [1, 1, 1, 0]
    # Case 1
    bond_list = [0] * len(rna_seq)
    for base_num in range(1, (len(rna_seq) // 2 + 1)):
        base1 = rna_seq[base_num - 1]
        base2 = rna_seq[-base_num]
        if bond_possible(base1, base2):
            bond_list[base_num - 1] = 1
            bond_list[-base_num] = 1
    for bond in bond_list:
        if bond == 0:
            case_test_output[0] = 0
    # Case 2
    bond_list = [0] * len(rna_seq)
    for base_num in range(1, (len(rna_seq)), 2):
        base1 = rna_seq[base_num - 1]
        base2 = rna_seq[base_num]
        if bond_possible(base1, base2):
            bond_list[base_num - 1] = 1
            bond_list[base_num] = 1
    for bond in bond_list:
        if bond == 0:
            case_test_output[1] = 0
    # Case 3
    bond_list = [0] * len(rna_seq)
    for base_num in range(1, len(rna_seq)):
        if not bond_list[base_num - 1]:
            base1 = rna_seq[base_num - 1]
            base2 = rna_seq[-base_num]
            base3 = rna_seq[base_num]
            if bond_possible(base1, base3):
                bond_list[base_num - 1] = 1
                bond_list[base_num] = 1
            elif bond_possible(base1, base2):
                bond_list[base_num - 1] = 1
                bond_list[-base_num] = 1
    for bond in bond_list:
        if bond == 0:
            case_test_output[2] = 0
    # Case 4
    bond_list = len(rna_seq) * [0]
    # print(delve(rna_seq, bond_list))
    if delve(rna_seq, bond_list):
        case_test_output[3] = 1

    # print(case_test_output)

    if 1 in case_test_output:
        return True
    else:
        return False


# If even and not perfect or if odd, check for almost perfect
def check_almost_perfect(rna_seq):
    for base_num in range(1, len(rna_seq)):
        even_seq = rna_seq[:(base_num - 1)] + rna_seq[base_num:]
        # print(even_seq)
        if check_perfect(even_seq):
            return True

# Main
RNA_length = len(RNA_string)
RNA_length_state = even_or_odd(RNA_string)
if RNA_length < 2:
    print('imperfect', end='')
elif RNA_length_state == 'even' and check_perfect(RNA_string):
    print('perfect', end='')
elif RNA_length_state == 'odd' and check_almost_perfect(RNA_string):
    print('almost perfect', end='')
else:
    print('imperfect', end='')


