# Rosalind - Bioinformatics Stronghold - 5 - Translating RNA into Protein
#
# Given: An RNA string s corresponding to a strand of mRNA (of length at most
#   10 kbp).
#
# Return: The protein string encoded by s.
#
# Updated 12/3/2016 by Jon Strutz


# Translation matrix
def translate_codon(codon):
    if codon == 'UUU' or codon == 'UUC':
        return 'F'
    elif codon == 'UUA' or codon == 'UUG' or codon == 'CUU' or \
         codon == 'CUC' or codon == 'CUA' or codon == 'CUG':
        return 'L'
    elif codon == 'UCU' or codon == 'UCC' or codon == 'UCA' or \
         codon == 'UCG' or codon == 'AGU' or codon == 'AGC':
        return 'S'
    elif codon == 'UAU' or codon == 'UAC':
        return 'Y'
    elif codon == 'UGU' or codon == 'UGC':
        return 'C'
    elif codon == 'UGG':
        return 'W'
    elif codon == 'CCU' or codon == 'CCC' or codon == 'CCA' or \
         codon == 'CCG':
        return 'P'
    elif codon == 'CAU' or codon == 'CAC':
        return 'H'
    elif codon == 'CAA' or codon == 'CAG':
        return 'Q'
    elif codon == 'CGU' or codon == 'CGC' or codon == 'CGA' or \
         codon == 'CGG' or codon == 'AGA' or codon == 'AGG':
        return 'R'
    elif codon == 'AUU' or codon == 'AUC' or codon == 'AUA':
        return 'I'
    elif codon == 'AUG':
        return 'M'
    elif codon == 'ACU' or codon == 'ACC' or codon == 'ACA' or \
         codon == 'ACG':
        return 'T'
    elif codon == 'AAU' or codon == 'AAC':
        return 'N'
    elif codon == 'AAA' or codon == 'AAG':
        return 'K'
    elif codon == 'GUU' or codon == 'GUC' or codon == 'GUA' or \
         codon == 'GUG':
        return 'V'
    elif codon == 'GCU' or codon == 'GCC' or codon == 'GCA' or \
         codon == 'GCG':
        return 'A'
    elif codon == 'GAU' or codon == 'GAC':
        return 'D'
    elif codon == 'GAA' or codon == 'GAG':
        return 'E'
    elif codon == 'GGU' or codon == 'GGC' or codon == 'GGA' or \
         codon == 'GGG':
        return 'G'
    elif codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
        return 'Stop'
    else:
        return '-'


def main():
    with open('05_PROT.txt') as inputfile:
        s = inputfile.read()

    # Initialize last_codon and translation
    last_codon_num = -1
    translation = []

    # Cycle through s and translate
    for i in range(0, len(s) + 1):
        codon_num = i // 3
        final_codon = (len(s)) // 3

        if codon_num != last_codon_num:
            codon = s[(codon_num * 3):(codon_num * 3 + 3)]
            amino_acid = translate_codon(codon)
            if amino_acid == 'Stop':
                break
            translation.append(amino_acid)
        last_codon_num = codon_num

    # Output translation
    translation = ''.join(translation)
    print(translation)

    output_file = open('05_PROT_output.txt', 'w')
    output_file.write(translation)
    output_file.close()


if __name__ == '__main__':
    main()
