# Rosalind - Bioinformatics Stronghold - 19 - Finding a Protein Motif
#
# Given: At most 15 UniProt Protein Database access IDs
#
# Return: For each protein possessing the N-glycosylation motif, output its
#   given ID followed by a list of locations in the protein string where the
#   motif can be found.
#
# Updated 1/19/2017 by Jon Strutz


import urllib.request
import regex as re


def get_data(filename):
    id_list = []
    with open(filename) as infile:
        for line in infile:
            line = line.strip()
            id_list.append(line)
    return id_list


def get_fasta(id_list):
    fasta_dict = {}
    for uniprot_id in id_list:
        fasta_dict[uniprot_id] = ''
        link = 'http://www.uniprot.org/uniprot/' + str(uniprot_id) + '.fasta'
        with urllib.request.urlopen(link) as infile:
            next(infile)
            fasta_dict[uniprot_id] = infile.read()
            for up_id in fasta_dict:
                fasta_dict[up_id] = str(fasta_dict[up_id]).replace('\\n', '')
                fasta_dict[up_id] = str(fasta_dict[up_id]).replace('b\'', '')
                fasta_dict[up_id] = str(fasta_dict[up_id]).replace('\'', '')
    return fasta_dict


def find_motif(fasta_dict):
    locations_dict = {}
    for uniprot_id in fasta_dict:
        current_seq = fasta_dict[uniprot_id]
        locations_dict[uniprot_id] = []
        for m in re.finditer("N[^P][ST][^P]", str(current_seq),
                             overlapped=True):
            locations_dict[uniprot_id].append(m.start() + 1)
    return locations_dict


def output_motif_locations(filename, locations_dict):
    with open(filename, 'w') as outfile:
        for uniprot_id in locations_dict:
            if len(locations_dict[uniprot_id]) >= 1:
                outfile.write(uniprot_id)
                outfile.write('\n')
                i = 1
                for location in locations_dict[uniprot_id]:
                    outfile.write(str(location))
                    if i < len(locations_dict[uniprot_id]):
                        outfile.write(' ')
                    i += 1
                outfile.write('\n')


if __name__ == '__main__':
    uniprot_ids = get_data('BS19_MPROT.txt')
    uniprot_fasta_dict = get_fasta(uniprot_ids)
    motif_locations_dict = find_motif(uniprot_fasta_dict)
    output_motif_locations('BS19_MPROT_out.txt', motif_locations_dict)