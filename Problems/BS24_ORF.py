# Rosalind - Bioinformatics Stronghold - 24 - Open Reading Frames
#
# Given: A DNA string s of length at most 1 kbp in FASTA format.
#
# Return: Every distince candidate protein string that can be translated from
#  ORFs of s. Strings can be returned in any order.
#
# Updated 3/29/2017 by Jon Strutz


from BS05_PROT import translate_codon


def get_string(filename):
    """Returns DNA sequence from input text file"""
    seq = ''
    with open(filename) as infile:
        for line_num, line in enumerate(infile):
            if line_num >= 1:
                seq += line.strip()
    return seq


def get_transcriptable_seqs(seq):
    """Transcribes DNA and returns transcribable sequences (from start codon 
    to start codon"""

    # Transcribe sequence
    seq_transcribed = ''
    for base_num1 in range(len(seq)):
        if seq[base_num1] == 'T':
            seq_transcribed += 'U'
        else:
            seq_transcribed += seq[base_num1]

    # Get all possible transcripts from DNA string
    transcript_seqs = []
    for base_num2, base2 in enumerate(seq_transcribed):
        # Find start codon
        if seq_transcribed[base_num2:base_num2 + 3] == 'AUG':
            sub_string = seq_transcribed[base_num2:]

            # Save each codon into one of the transcript_seqs until a stop
            # codon is hit
            transcript = ''
            for base_num3, base3 in enumerate(sub_string):
                if base_num3 % 3 == 0:
                    codon = sub_string[base_num3:base_num3 + 3]
                    if codon == 'UAG' or codon == 'UGA' or codon == 'UAA':
                        transcript_seqs.append(transcript)
                        break
                    else:
                        transcript += codon

    return transcript_seqs


def reverse_complement(seq):
    rev_comp = ''
    # Want to go in reverse
    for i in range(len(seq) - 1, -1, -1):
        if seq[i] == 'A':
            rev_comp += 'T'
        elif seq[i] == 'C':
            rev_comp += 'G'
        elif seq[i] == 'G':
            rev_comp += 'C'
        elif seq[i] == 'T':
            rev_comp += 'A'
    return rev_comp


def get_translations(seqs):
    translated_seqs = []
    for seq in seqs:
        translated_seqs.append('')
        for base_num, base in enumerate(seq):
            if base_num % 3 == 0:
                codon = seq[base_num:base_num + 3]
                amino_acid = translate_codon(codon)
                translated_seqs[-1] += amino_acid
    return translated_seqs


def eliminate_duplicates(seqs):
    for seq_num1, seq1 in enumerate(seqs):
        for seq2 in seqs[seq_num1 + 1:]:
            if seq1 == seq2:
                del seqs[seq_num1]
    return seqs


def print_to_file(filename, seqs):
    with open(filename, 'w') as outfile:
        for seq in seqs:
            outfile.write(seq + '\n')


if __name__ == '__main__':
    DNA_string = get_string('BS24_ORF.txt')
    DNA_string_rev = reverse_complement(DNA_string)

    transcripts = get_transcriptable_seqs(DNA_string)
    transcripts_rev = get_transcriptable_seqs(DNA_string_rev)

    translations = get_translations(transcripts)
    translations_rev = get_translations(transcripts_rev)

    all_translations = translations + translations_rev

    distinct_translations = eliminate_duplicates(all_translations)

    print_to_file('BS24_ORF_out.txt', distinct_translations)
