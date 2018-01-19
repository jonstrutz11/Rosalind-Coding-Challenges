# Rosalind - Bioinformatics Stronghold - 25 - Locating Restriction Sites
#
# Given: A DNA string of length at most 1 kbp in FASTA format.
#
# Return: The position and length of every reverse palindrome in the string
# having length between 4 and 12. You may return these pairs in any order.
#
# Updated 4/12/2017 by Jon Strutz


def is_palindrome(string):
    first_half = string[0:len(string) // 2]
    second_half = string[len(string) // 2:len(string)]
    first_half_rc = ''
    # Find reverse complement of each base in first half and add to beginning
    #  of reverse complement string (to be compared with second half)
    for char in first_half:
        if char == 'A':
            char_rc = 'T'
        elif char == 'C':
            char_rc = 'G'
        elif char == 'G':
            char_rc = 'C'
        elif char == 'T':
            char_rc = 'A'
        else:
            raise ValueError("Characters in sequence must be A, C, G, or T.")
        first_half_rc = char_rc + first_half_rc
    # Test to see if reverse complement of the first half is identical to the
    #  second half (i.e. the whole string is a palindrome)
    if first_half_rc == second_half:
        return True
    else:
        return False


if __name__ == '__main__':
    with open('BS25_REVP.txt', 'r') as infile:
        infile.readline()
        dna_seq = ''
        for line in infile:
            dna_subseq = line.strip()
            dna_seq += dna_subseq
        print(dna_seq)
    dna_len = len(dna_seq)
    # Check if all possible sequences and subsequences are palindromes
    palindrome_list = []
    for index, bp in enumerate(dna_seq):
        for length in [4, 6, 8, 10, 12]:
            current_seq = ''
            if index + length <= dna_len:
                current_seq = dna_seq[index:index + length]
                if is_palindrome(current_seq):
                    palindrome_list.append(index)
                    palindrome_list.append(length)
    # Write outfile in format [position] [palindrome length] on each line
    with open('BS25_REVP_out.txt', 'w') as outfile:
        for index, value in enumerate(palindrome_list):
            if index % 2 == 0:
                outfile.write(str(value + 1) + ' ')
            else:
                outfile.write(str(value) + '\n')
