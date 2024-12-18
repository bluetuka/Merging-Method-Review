import networkx as nx

def main():
    s = 0
    t = 5
    V = [0, 1, 2, 3, 4, 5]
    G = nx.Graph()

    for v in V:
        G.add_node(v)
    
    G.add_edge(s, 1)
    G.add_edge(s, 2)
    G.add_edge(1, 2)
    G.add_edge(1, 4)
    G.add_edge(2, 4)
    G.add_edge(2, 3)
    G.add_edge(4, 3)
    G.add_edge(3, t)
    G.add_edge(4, t)

    i = k = 0
    S = [s]
    T = [1, 2, 3, 4, t]
    
    Est = []
    for t in T:
        if G.has_edge(s, t):
            Est.append((s, t))
    
    A = C0 = D0 = Est
    N0 = [t]
    B = []
    T = [C0]


if __name__ == "__main__":
    main()