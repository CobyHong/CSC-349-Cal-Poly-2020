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
        if second not in dictionary.keys():
            dictionary[second] = []
    return dictionary


def getTranspose():
    dictionary = {}
    file = open(sys.argv[1], "r")
    content = file.readlines()
    for i in range(0, len(content)):
        curr_line = content[i].split(',')

        second = int(curr_line[0])
        first = int(curr_line[1])

        if first in dictionary.keys():
            dictionary[first].append(second)
        else:
            dictionary[first] = [second]
        if second not in dictionary.keys():
            dictionary[second] = []
    return dictionary


def util_explore(graph, vertex, visited, component_list):
    visited[vertex] = True
    component_list.append(vertex)

    for i in graph[vertex]:
        if visited[i] == False:
            util_explore(graph, i, visited, component_list)


def filler_explore(graph, vertex, visited, stack):
    visited[vertex] = True

    for i in graph[vertex]:
        if visited[i] == False:
            filler_explore(graph, i, visited, stack)
    stack = stack.append(vertex)


def kosaraju(graph, reverse_graph):
    stack = []
    vertex_length = len(graph)

    visited =[False] * (vertex_length)
    for i in range(vertex_length):
        if visited[i] == False:
            filler_explore(graph, i, visited, stack)
    
    visited =[False] * (vertex_length)
    component_result = []
    component_counter = 0
    while stack:
        i = stack.pop()
        if visited[i] == False:
            component_list = []
            util_explore(reverse_graph, i, visited, component_list)
            component_list.sort()
            component_result.append(component_list)
            component_counter += 1
    component_result.sort()
    printWork(component_result, component_counter)


def printWork(component_result, component_counter):
    print(component_counter, end = " ")
    print("Strongly Connected Component(s):")

    for x in range(len(component_result)):
        if len(component_result[x]) == 1:
            print(component_result[x][0])
        else:
            last = 0
            for y in range(len(component_result[x]) - 1):
                print(component_result[x][y], end = ", ")
                last = y
            print(component_result[x][last + 1])


forward = createDictionary()
reverse = getTranspose()
kosaraju(forward, reverse)
