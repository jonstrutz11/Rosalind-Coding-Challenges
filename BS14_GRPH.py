# Rosalind - Bioinformatics Stronghold - 14 - Overlap Graphs
#
# Given: A collection of DNA strings in FASTA format having total length at
#   most 10 kbp.
#
# Return: The adjacency list corresponding to O3. You may return edges in any
#   order.
#
# Updated 12/17/2016 by Jon Strutz

k = 3


def get_seq_dict(fasta_seqs):
    """Stores input FASTA data in an id:sequence dictionary"""
    seq_dict = {}
    seq_list = fasta_seqs.split('\n')
    for fasta_num in range(0, len(seq_list)):
        # Eliminate index error at end of loop
        if fasta_num + 1 == len(seq_list):
            pass
        # if on the 2nd, 5th, 8th, etc. line then get those lines
        elif fasta_num % 3 == 0:
            seq_dict[seq_list[fasta_num].replace('>', '')] \
                = seq_list[fasta_num + 1] + seq_list[fasta_num + 2]
    return seq_dict


def overlap(seq_dict):
    """Finds overlaps between the first and last k elements of each sequence
    from an id:sequence dictionary and stores the ids for those sequences in a
    list"""
    adjacency_list_list = []
    for key1 in seq_dict:
        for key2 in seq_dict:
            if key1 == key2:
                pass
            elif seq_dict[key1][0:k] == seq_dict[key2][-k:]:
                adjacency_list_list.append(key2 + ' ' + key1)
    return adjacency_list_list


def print_list(unformatted_list, filename):
    """Formats the list to provide the two elements on a newline"""
    with open(filename, 'w') as outfile:
        for edge in unformatted_list:
            outfile.write(edge + '\n')

# Main code
with open('14_GRPH.txt') as infile:
    fasta_seqs = infile.read()

adjacency_list_unformatted = overlap(get_seq_dict(fasta_seqs))
print_list(adjacency_list_unformatted, '14_GRPH_output.txt')