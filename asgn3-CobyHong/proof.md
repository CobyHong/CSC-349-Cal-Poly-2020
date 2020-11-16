# Pseudo Code:

```Python

Inputs:
-graph <- {a1 : {b1, ..., bn}, ... an}) == (a dictionary)
-vertex <- current location in graph.
-visited_list <- {"False", ..., "False"}
-current_component_color_list <- {-1, ..., -1} == -1 means not colored.
-color <- either a 0 or 1.

DFS(graph):
    let color_result = empty list.

    let vertex_length = len(A)
    let visited_list = Array of "False" length of vertex_length.

    for vertex in Graph do:
        if visited_list[vertex] is "False":
            current_component_color_list = {}
            explore(graph, vertex, visited, current_component_color_list, 0)

            then remove all -1's from current_component_color_list.
            color_result.add(current_componenet_color_list)
    return color_result

explore(graph, vertex, visited_list, current_component_color_list, color):
    let visited_list[vertex] = "True"
    let current_component_color_list[vertex] = color

    for neighbors in graph[vertex] do:
        if visited_list[neighbors] is "False":
            explore(graph, neighbors, visited_list, current_component_color_list, 1-color)

Example of Input & Output:
Input:
    "0, 1"
    "1, 2"
    "2, 3"
    "3, 0"
    "4, 5"
Output:
    [ {0,1,0,1} , {0,1} ]

```

# Proof:

Thereom:
Prove DFS function is correct.

Lemma:
If a graph G = (V, E) is 2-colorable, explore function called in DFS colors every vertex v ∈ V exactly once.

Proof:
Suppose G is a 2-colorable and has >= 1 cycles. WLOG, suppose v1 ∈ V1, then the cycle begins and ends in the set V. Since G is 2-colorable, in order to return to v1, the cycle must traverse an even number of edges, whichmeans that each vertex is colored exactly once. [✔]

Suppose for contradiction, there exist a v ∈ V that is not explored exactly once. This will lead to two possibilities existing:
    (1). V is never colored. This cannot occur as the explore function is called on every vertex and every vertex is initially not colored. This means upon calling the explore function, the vertex will be colored.
    (2). V is colored more than once. This cannot occur as the explore function is only called on vertexes whose visited status is set to "False". Vertices are immediately have their visited status set to "True" once the explore function is called on them. Vertices with the visited status of "True" are never set to "False" status.

Therefore, by proof of contradiction, every vertex is colored exactly once. [✔]

Considerations:
Suppose, for contradiction, G is not 2-colorable and >= 1 cycles. If G is not 2-colorable, in order to return to v1, the cycle must traverse and odd number of edges. This means the back edge's pre-parity and post-parity equals that of its ancestors. However, G can only be 2-colorable if and onlly if there are no cycles of odd length, which is correctly identified by the algorithm.

Therefore, our function correctly identifies if the graph is 2-colorable or not [✔]



# Time Complexity:

O(|V| + |E|)
-explore called on each vertex once.
-explore considers every edge once or twice.
-dfs considers each vertex twice.
