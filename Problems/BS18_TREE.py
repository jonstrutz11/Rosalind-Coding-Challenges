# Rosalind - Bioinformatics Stronghold - 18 - Completing a Tree
#
# Given: A positive integer n (n <= 1000) and an adjacency list corresponding
#   to a graph of n nodes that contains no cycles.
#
# Return: The minimum number of edges that can be added to the graph to
#   produce a tree.
#
# Updated 1/19/2017 by Jon Strutz


def get_data():
    """Get data from file, BS18_TREE.txt, and return n and adjacency list"""
    with open('BS18_TREE.txt') as infile:
        i = 0
        for line in infile:
            if i == 0:
                n = int(line)
                adj_list = {}
            elif i > 0:
                line = line.strip()
                edge = line.split(' ')
                if edge[0] in adj_list:
                    adj_list[edge[0]].append(edge[1])
                else:
                    adj_list[edge[0]] = [edge[1]]
            i += 1
    return n, adj_list


def count_fragments(n, adj_list):
    """Counts number of edges in adjacency list and then calculates the
    number of fragments (nodes - edges)"""
    edges = 0
    for key in adj_list:
        edges += len(adj_list[key])
    print(edges)
    fragments_count = n - edges
    return fragments_count


if __name__ == "__main__":
    nodes, adjacency_list = get_data()
    num_fragments = count_fragments(nodes, adjacency_list)
    min_edges = num_fragments - 1
    print(min_edges)
