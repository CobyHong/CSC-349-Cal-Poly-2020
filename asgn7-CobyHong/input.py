import sys
import itertools
import graph
import subgraph_isomorphism as si


def k_value():
    file = open(sys.argv[1], "r")
    content = file.readlines()
    clause_count = int((content[0].count('(') + content[0].count(')')) / 2)
    return clause_count


def get_cliques(k_value):
    graph_h = graph.Graph()
    vertices = []

    for i in range(0, k_value):
        graph.add_vertex(graph_h, i)
        vertices.append(i)
    for i in graph_h:
        temp = vertices.copy()
        temp.remove(i)
        temp.sort()
        graph_h[i] = temp

    return graph_h


def is_iso(graph_g):
    k = k_value()
    graph_h = get_cliques(k)
    subgraph = si.isomorphic_subgraph(graph_g, graph_h)

    return subgraph


def sat():
    graph_g = graph.Graph()
    my_dic = []

    #reading in file.
    file = open(sys.argv[1], "r")
    content = file.readlines()
    clause_count = int((content[0].count('(') + content[0].count(')')) / 2)
    content[0] = content[0].strip('\n')

    #turning into array.
    clauses = content[0].split('&')
    for i in range(0, len(clauses)):
        clauses[i] = clauses[i].replace('|', '')
        clauses[i] = clauses[i].replace('(', '')
        clauses[i] = clauses[i].replace(')', '')
        clauses[i] = clauses[i].split()
        for j in clauses[i]:
            my_dic.append(j)
    
    #turning into unique numbers for dictionary.
    for i in range(len(clauses)):
        for j in range(3):
            graph.add_vertex(graph_g, str(i*3+j))

    #traversing...
    for i in range(len(clauses)):
        for j in range(len(clauses[i])):
            for k in range(len(clauses)):
                if(i != k):
                    for l in range(len(clauses[k])):

                        negation = ""
                        if(len(clauses[k][l]) == 2):
                            negation = clauses[k][l][1:]
                        else:
                            negation = "~" + clauses[k][l]
                        if(clauses[i][j] != negation):
                            graph.add_edge(graph_g, str(i*3+j), str(k*3+l))
    
    #run isomorph on it.
    subgraph = is_iso(graph_g)

    #printing process.
    result = []
    if(subgraph is None):
        print("No satisfying assignments.")
        return
    for i in subgraph:
        string = my_dic[int(i)]
        result.append(string)
    result.sort(key=lambda x: x[-1])
    print("Satisfying assignment:")
    print(", ".join(result))


sat()