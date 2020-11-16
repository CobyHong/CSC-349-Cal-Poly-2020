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


def accumulator(dictionary):
    degrees = []
    for key in dictionary:
        counter = len(dictionary[key])
        degrees.append(tuple((key, counter)))
    degrees.sort(key=lambda tup: tup[0])
    degrees.sort(key=lambda tup: tup[1])
    return degrees


def vertex_remover(dictionary, v):
    dictionary.pop(v, None)
    for key in dictionary:
        if v in dictionary[key]:
            dictionary[key].remove(v)


def kCores(dictionary):
    k = 1
    kcores = {}
    remove_list = []
    degrees = accumulator(dictionary)

    while degrees:
        #always index 0 because popping.
        vertex = degrees[0][0]
        degree = degrees[0][1]

        if degree <= k:
            #add that key to our removed list.
            remove_list.append(degrees.pop(0))
            vertex_remover(dictionary, vertex)
            degrees = accumulator(dictionary)
        else:
            kcores[k] = sorted([i for i, d in remove_list])
            k += 1
            remove_list = []
    
    if(len(remove_list) > 0):
        kcores[k] = []
        for i, d in remove_list:
            kcores[k].append(i)
        kcores[k].sort()

    for i in kcores.keys():
        for j in range(i+1, k+1):
            kcores[i].extend(kcores[j])
    return kcores


def printWork(dictionary):
    for key in dictionary:
        dictionary[key].sort()
        print("Vertices in ", key, "-cores:", sep="")
        print(*dictionary[key], sep=", ")


dictionary = createDictionary()
result = kCores(dictionary)
printWork(result)
