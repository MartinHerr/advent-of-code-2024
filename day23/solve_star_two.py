#!/usr/bin/env python3
from parser import parse_input

# Cache of n-1 size cliques, to avoid re-computing the previous cliques
# when we increment the tested size.
clique_cache = {}

def find_cliques(graph, size):
    """
    Find all cliques of a given size in the graph.
    A clique is a subset of nodes where every two nodes are connected.
    """
    if size == 2:
        # Arbitrarily selection of a size 2 clique
        if size not in clique_cache:
            clique_cache[size] = {(min(node, neighbor), max(node, neighbor)) for node, neighbors in graph.items() for neighbor in neighbors}
        return clique_cache[size]
    smaller_cliques = clique_cache[size - 1]
    cliques = set()
    for clique in smaller_cliques:
        for node in graph:
            if node not in clique and all(neighbor in graph[node] for neighbor in clique):
                new_clique = tuple(sorted(clique + (node,)))
                cliques.add(new_clique)
    clique_cache[size] = cliques
    return cliques

def find_largest_clique(graph):
    """
    Find the largest clique in the graph.
    """
    largest_clique = []
    size = 2 
    while True:
        cliques = find_cliques(graph, size)
        if not cliques:
            break
        largest_clique = max(cliques, key=len)
        size += 1
    return sorted(largest_clique)

if __name__ == "__main__":
    with open("input.txt") as input:
        seen_computers, links = parse_input(input)
    largest_clique = find_largest_clique(links)
    print(",".join(sorted(largest_clique)))
