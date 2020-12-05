import networkx

G = networkx.DiGraph()

for a in open("06_input.txt").readlines():
    G.add_edge(*[x.strip() for x in a.split(')')])

print(networkx.transitive_closure(G).size())

print(networkx.shortest_path_length(G.to_undirected(), "YOU", "SAN")-2)