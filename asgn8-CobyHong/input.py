import sys
import itertools
from graph import *


def explore(graph, vertex, visited, my_list):
    visited[vertex] = True

    for i in graph[vertex]:
        my_list.append(i)
        if visited[i] == False:
            explore(graph, i, visited, my_list)
            

def DFS(graph, vertices_count):
    visited = [False] * vertices_count
    my_list = [0]

    for vertex in range(vertices_count):
        if visited[vertex] == False:
            explore(graph, vertex, visited, my_list)
    return my_list


def edge_doubler(graph):
    result = []
    for i in range(len(graph)):
        result.append(graph[i])
        result.append([graph[i][1],
                       graph[i][0],
                       graph[i][2]])
    result.sort()
    return result


def make_into_graph(doubled_graph):
    graph_result = Graph()
    for i in range(len(doubled_graph)):
        add_edge(graph_result,
                       doubled_graph[i][0],
                       doubled_graph[i][1],
                       doubled_graph[i][2])
    return graph_result


def kruskal(graph, vertices_count):
    result = []

    i = 0
    e = 0

    graph = sorted(graph, key=lambda item: item[2])

    parent = []
    rank = []

    for node in range(vertices_count):
        parent.append(node)
        rank.append(0)
    
    while e < vertices_count - 1:
        u,v,w = graph[i]
        i = i + 1

        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e = e + 1
            result.append([u,v,w])
            union(parent, rank, x, y)

    return result


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y): 
    xroot = find(parent, x) 
    yroot = find(parent, y) 
  
    if rank[xroot] < rank[yroot]: 
        parent[xroot] = yroot 
    elif rank[xroot] > rank[yroot]: 
        parent[yroot] = xroot 
  
    else : 
        parent[yroot] = xroot 
        rank[xroot] += 1


def total_weight(graph):
    weight = 0
    graph_weights = read_graph(sys.argv[1])

    for i in range(len(graph) - 1):
        weight += graph_weights[graph[i]][graph[i + 1]]
    return weight


def get_graph():
    graph = []
    vertices = 0
    list_of_vertices = {}

    file = open(sys.argv[1], "r")
    content = file.readlines()
    for i in range(len(content)):
        line = content[i].strip()
        line = content[i].split(',')
        graph.append([int(line[0]),int(line[1]),int(line[2])])

        if int(line[0]) not in list_of_vertices.keys():
            list_of_vertices[int(line[0])] = []
            vertices += 1

        elif int(line[1]) not in list_of_vertices.keys():
            list_of_vertices[int(line[1])] = []
            vertices += 1

    return graph, vertices


graph = get_graph()
kruskal_result = kruskal(graph[0], graph[1])
double_edges_result = edge_doubler(kruskal_result)
graph_conversion_result = make_into_graph(double_edges_result)
dfs_result = DFS(graph_conversion_result, graph[1])

res = [] 
[res.append(x) for x in dfs_result if x not in res]

res.append(res[0])
weight = total_weight(res)

print("Hamiltonian cycle of weight {}:".format(weight))
output = []
for i in res:
    output.append(str(i))
print(", ".join(output))

