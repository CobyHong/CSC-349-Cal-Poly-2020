import sys


def createDictionary():
    dictionary = {}
    file = open(sys.argv[1], "r")
    content = file.readlines()
    for i in range(0, len(content)):
        curr_line = content[i].split(',')

        first = int(curr_line[0])
        second = int(curr_line[1])

        if first in dictionary.keys():
            dictionary[first].append(second)
        else:
            dictionary[first] = [second]

        if second in dictionary.keys():
            dictionary[second].append(first)
        else:
            dictionary[second] = [first]
    return dictionary


def explore(graph, vertex, visited, component_list, color_list, c):
    component_list.append(vertex)
    visited[vertex] = True
    color_list[vertex] = c

    for i in graph[vertex]:
        if visited[i] == False:
            explore(graph, i, visited, component_list, color_list, 1-c)
    return component_list


def DFS(graph):
    vertex_length = len(graph)
    color_list = [-1] * len(graph)
    visited = [False] * (vertex_length)
    components_result = []

    for vertex in range(vertex_length):
        if visited[vertex] == False:
            component_list = []
            explore(graph, vertex, visited, component_list, color_list, 0)
            components_result.append(component_list)
    printWork(graph, components_result, color_list)


def printWork(graph, components_result, color_list):
    for i in range(len(graph)):
        for j in graph[i]:
            if color_list[i] == color_list[j]:
                print("Is not 2-colorable.")
                return

    result = []
    for x in range(len(components_result)):
        zeros_list = []
        ones_list = []
        for y in range(len(components_result[x])):
            if color_list[components_result[x][y]] == 0:
                zeros_list.append(components_result[x][y])
            if color_list[components_result[x][y]] != 0:
                ones_list.append(components_result[x][y])
        zeros_list.sort()
        ones_list.sort()
        result.append(zeros_list)
        result.append(ones_list)
    result.sort()

    print("Is 2-colorable:")
    for a in range(len(result)):
        if len(result[a]) == 1:
            print(result[a][0])
        else:
            last = 0
            for b in range(len(result[a]) - 1):
                print(result[a][b], end =", ")
                last = b
            print(result[a][last + 1])


dictionary = createDictionary()
DFS(dictionary)