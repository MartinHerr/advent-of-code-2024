#!/usr/bin/env python3
def parse_input(input):
    graph = {}
    for line in input:
        a, b = line.strip().split("-")
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)
    return graph

def bron_kerbosch(graph, R, P, X, cliques):
    """
    Bron-Kerbosch algorithm with pivoting to find all maximal cliques.
    R: current clique being built
    P: potential candidates for expansion
    X: already visited nodes to exclude
    cliques: list to collect maximal cliques
    https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
    """
    if not P and not X:
        cliques.append(R)
        return
    # Choose a pivot, chosen from P ⋃ X (node with the highest degree in P ⋃ X)
    pivot = max(P | X, key=lambda node: len(graph[node]))
    for vertex in P - graph[pivot]:
        bron_kerbosch(graph, R | {vertex}, P & graph[vertex], X & graph[vertex], cliques)
        P.remove(vertex)
        X.add(vertex)

def find_largest_clique(graph):
    """
    Find the largest clique in the graph using Bron-Kerbosch algorithm.
    """
    cliques = []
    nodes = set(graph.keys())
    bron_kerbosch(graph, set(), nodes, set(), cliques)
    return max(cliques, key=len)

if __name__ == "__main__":
    with open("input.txt") as input:
        graph = parse_input(input)
    # for i, key in enumerate(graph):
    #     print(f"{i} - {key}: {graph[key]}")
    largest_clique = find_largest_clique(graph)
    print(",".join(sorted(largest_clique)))
