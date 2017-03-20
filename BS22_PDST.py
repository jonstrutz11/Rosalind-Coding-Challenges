# Rosalind - Bioinformatics Stronghold - 22 - Creating a Distance Matrix
#
# Given: A collection of n (n ≤ 10) DNA strings s1,…,sn of equal length (at
#   most 1 kbp). Strings are given in FASTA format.
#
# Return: The matrix D corresponding to the p-distance dp on the given
#   strings. As always, note that your answer is allowed an absolute error of
#   0.001.
#
# Updated 3/20/2017 by Jon Strutz


def seqs_from_fasta(filename):
    seq_list = []
    current_seq = ''
    first_line = True
    with open(filename) as infile:
        for line in infile:
            if line[0] == '>' and not first_line:
                seq_list.append(current_seq)
                current_seq = ''
            elif first_line:
                first_line = False
            else:
                current_seq += line.strip()
        seq_list.append(current_seq)
    return seq_list


def calculate_distance(seq1, seq2):
    distance = 0
    for bp_index in range(len(seq1)):
        if seq1[bp_index] == seq2[bp_index]:
            continue
        else:
            distance += 1
    return distance / len(seq1)


def calculate_matrix(seq_list):
    dist_matrix = [[0.00 for i in range(len(seq_list))] for i in range(len(
                    seq_list))]
    for seq1_index in range(len(seq_list)):
        for seq2_index in range(len(seq_list)):
            seq1 = seq_list[seq1_index]
            seq2 = seq_list[seq2_index]
            dist_matrix[seq1_index][seq2_index] = calculate_distance(seq1, seq2)
    return dist_matrix


def show_matrix(dist_matrix):
    for row_num in range(len(dist_matrix)):
        line_vals = [value for value in dist_matrix[row_num]]
        i = 0
        for val in line_vals:
            if i != len(line_vals) - 1:
                print("%.5f" % val, end=' ')
                i += 1
            else:
                print("%.5f" % val)


if __name__ == '__main__':
    sequence_list = seqs_from_fasta('BS22_PDST.txt')
    distance_matrix = calculate_matrix(sequence_list)
    show_matrix(distance_matrix)
