# Rosalind - Bioinformatics Stronghold - 20 - Finding a Most Likely Common
#                                             Ancestor
#
# Given: A collection of at most 10 DNA strings of equal length (at most 1
#   kbp) in FASTA format
#
# Return: A consensus string and profile matrix for the collection. (If
#   several possible consensus strings exist, then you may return any one of
#   them.)
#
# Updated 2/8/2017 by Jon Strutz


def get_fasta_seqs(file):
    """Returns a dictionary of format ID : sequence from a FASTA file. The ID
    portion is the whole line above the sequence"""
    seq_dict = {}
    current_id = None
    with open(file) as infile:
        for line in infile:
            line = line.strip()
            if '>' in line:
                current_id = line
                seq_dict[current_id] = ''
            else:
                seq_dict[current_id] += line
    return seq_dict


def get_seq_matrix(seq_dict):
    """Gets matrix of DNA strings (as rows of bases)"""
    num_seqs = len(seq_dict)
    seq_matrix = ['' for x in range(num_seqs)]
    i = 0
    for key in seq_dict:
        seq_matrix[i] = seq_dict[key]
        i += 1
    return seq_matrix


def get_profile(seq_dict, seq_len):
    """Gets profile for DNA string matrix (four rows labeled A, C, G, T where
    counts in each row are occurrences of that letter in same column of DNA
    matrix"""
    profile = [[0 for x in range(seq_len)] for y in range(4)]
    for base_num in range(seq_len):
        for key in seq_dict:
            if seq_dict[key][base_num] == 'A':
                profile[0][base_num] += 1
            elif seq_dict[key][base_num] == 'C':
                profile[1][base_num] += 1
            elif seq_dict[key][base_num] == 'G':
                profile[2][base_num] += 1
            elif seq_dict[key][base_num] == 'T':
                profile[3][base_num] += 1
    return profile


def get_consensus(profile, seq_len):
    """Find most common letter for each position in the DNA sequences and
    create DNA sequence of most common bases"""
    consensus = ''
    for base_num in range(seq_len):
        max_value = max(profile[x][base_num] for x in range(4))
        for base in range(len(profile)):
            if profile[base][base_num] == max_value:
                most_common_base_num = base
        if most_common_base_num == 0:
            most_common_base = 'A'
        elif most_common_base_num == 1:
            most_common_base = 'C'
        elif most_common_base_num == 2:
            most_common_base = 'G'
        else:
            most_common_base = 'T'
        consensus += most_common_base
    return consensus


def format_profile_and_write(profile, file, consensus):
    """Generate formatted output specified by problem statement"""
    with open(file, 'w') as outfile:
        outfile.write(consensus + '\n')
        for letter in ['A', 'C', 'G', 'T']:
            outfile.write('%s:' % letter)
            for value in profile[['A', 'C', 'G', 'T'].index(letter)]:
                outfile.write(' %s' % value)
            if letter != 'T':
                outfile.write('\n')


if __name__ == '__main__':
    seqs = get_fasta_seqs('BS20_CONS.txt')
    seq_length = len(next(iter(seqs.values())))
    dna_matrix = get_seq_matrix(seqs)
    prof = get_profile(seqs, seq_length)
    cons = get_consensus(prof, seq_length)
    format_profile_and_write(prof, 'BS20_CONS_out.txt', cons)
