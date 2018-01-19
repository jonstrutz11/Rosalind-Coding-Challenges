# Rosalind - Bioinformatics Stronghold - 17 - RNA Splicing
#
# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings
#   of s acting as introns. All strings are given in FASTA format.
#
# Return: A protein string resulting from transcribing and translating the exons
#   of s. (Note: Only one solution will exist for the dataset provided.)
#
# Updated 1/11/2017 by Jon Strutz


def get_seqs_from_fasta(filename):

    ids = []
    seqs = []
    current_seq = ''

    # Split up ids and seqs into two separate lists
    with open(filename) as infile:
        for line in infile:
            if line[0] == '>':
                if current_seq != '':
                    seqs.append(current_seq)
                ids.append(line[1:])
                current_seq = ''
            else:
                current_seq += line
        seqs.append(current_seq)

    # Clean up newlines in seqs
    trantab = {ord('\n'): ''}
    for i in range(len(seqs)):
        seqs[i] = seqs[i].translate(trantab)

    return seqs


def transcribe(dna_seqs):
    rna_seqs = [None for seq_num in range(len(dna_seqs))]

    for seq_num in range(len(dna_seqs)):
        rna_seqs[seq_num] = dna_seqs[seq_num].replace('T', 'U')

    return rna_seqs


def splice(rna_seqs):
    for seq_num in range(1, len(rna_seqs)):
        rna_seqs[0] = rna_seqs[0].replace(rna_seqs[seq_num], rna_seqs[
            seq_num].lower())

    spliced_rna = rna_seqs[0]
    trantab = {ord('a'): '', ord('c'): '', ord('g'): '', ord('u'): ''}
    spliced_rna = spliced_rna.translate(trantab)

    return spliced_rna


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
        return ''


def main():

    dna_seqs = get_seqs_from_fasta('17_SPLC.txt')

    rna_seqs = transcribe(dna_seqs)

    spliced_rna = splice(rna_seqs)

    protein_seq = ''

    for i in range(len(spliced_rna)):
        if i % 3 == 0:
            if i < (len(spliced_rna)):
                codon = spliced_rna[i:(i + 3)]
                amino_acid = translate_codon(codon)
                if amino_acid == 'Stop':
                    continue
                protein_seq += amino_acid

    print(dna_seqs)
    print('\n')
    print(rna_seqs)
    print('\n')
    print(spliced_rna)
    print('\n')
    print(protein_seq)


if __name__ == "__main__":
    main()
