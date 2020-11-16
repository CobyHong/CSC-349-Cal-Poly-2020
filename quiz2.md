# Question 2

CounterExample:
    Suppose graph G is a directed graph containing exactly two strongly connected components.
    This means that for each component, every vertex v ∈ V is reachable from every other vertex in that componenet.
    If were were to connect the components by a single edge, then a path should exist for any first chosen vertex to the second, and second to first vertex.
    for example:
        Let a graph G = (V,E) have...
            V = {1,2,3,4,5}
            E = {(1,2), (2,3), (3,1), (4,5), (5,4), (3,5)}
    
    In the current state of the graph G, we have two strongly connected components but the graph G as a whole is weakly connected. However, if we were to add an edge from 4 to 1, every vertex v ∈ V becomes reachable from every other vertex. This means the graph has become strongly connected by adding a single edge.


# Question 3

(A)
```Python
def DFS(directed graph G <- (V, E)):

Input: A directed graph G <- (V, E)
Output: A forest of vertices G

    for all vertex v ∈ V do:
        let vertex be given a "False" boolean value.
    
    for all vertex v ∈ V do:
        if vertex is "False", then do:
            let explore(directed graph, vertex) be a new tree in forest
    return forest

def explore(directed graph G <- (V, E), v):

Input: A directed graph G <- (V, E) and a vertex v in G where every vertex is either "True" or "False".
Output: A tree of vertices reachable from v

    let v have its boolean value set to "True", a tree node with no children.

    Previsit(v)
    for all successors of v, u, do:
        if u is "False", then do:
            let explore(directed graph, G), be a subtree of v.
    
    Postvisit(v)
    return the tree rooted v.

def test_strength(directed graph G <- (V, E), e):

Input: A directed graph G <- (V, E) and an edge e <- (u, v) inside of E.
Output: Return boolean value "True" if graph is still strongly connected after removing edge e.
        Return boolean value "False" f graph is NOT strongly connected after removing edge e.

        let new_graph_with_e_removed = directed graph G <- (V, E)
        remove edge e from new_graph_with_e_removed.

        let dfs_1 <- DFS(new_graph_with_e_removed)

        for v ∈ dfs_1 do:
            if v is "False", then do:
                return False
        
        let graph_transpose = directed graph G <- (V, E), but transposed.
        let dfs_2 <- DFS(graph_transpose)

        for v ∈ dfs_2 do:
            if v is "False", then do:
                return False
        
        return True
```
(B)
    Time Complexity:
        O(V+E)

        -Explore is called once for on every vertex.
        -Explore considers every edge once or twice.
        -DepthFirstSearch has to look at every vertex twice.
