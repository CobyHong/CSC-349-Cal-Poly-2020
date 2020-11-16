# Coby Hong
# CSC-349
# Quiz #3

# Question 1:

# (A):

```Python
Input: A tree T <- (V, E).
Output: An array of constructed matchings.

def matchings(tree T <- (V, E)):
    let matchings[] be an empty array.

    while edges ∈ E is not NULL, do:
        # meaning it only has one edge incident to it.
        let leaf_node be the node that has a degree of 1.
        let leaf_parent_node be the parent node to leaf_node.
        let leaf_edge be the edge incident to our leaf_node.

        #add to matchings list.
        append leaf_edge to our matchings[] list.

        #remove associated edges of u and v to leaf.
        remove leaf_edge from edges.
        remove other edges incident to leaf_node and leaf_parent_node.

        #remove u and v nodes associated to leaf.
        remove leaf_node and leaf_node_parent from V.

    #did not get all vertices.
    if len(V) in tree T does not equal 0, then do: 
        return "No perfect matching exists".
    return matchings[].
```

# (B):

Our algorithm makes the locally optimal choice of creating pairs based on leaf nodes. This works since the leaf node will always have exactly one edge to pair with its parent. After acquiring the leaf-edge, we remove all edges incident to the leaf and its parent node and the nodes themselves. This is done until there are no more edges to traverse. Therefore, the algorithm is locally optimal due to its edge-by-edge basis that guarantees one edge pairing between a leaf node and its parent.

# (C):

Time Complexity: O(V).
-visit at least twice on each node (once to find, once when removed and matched).

# Question 2:

Counter Example:
    Suppose graph G is an undirected graph that need not be connected and acyclic.
    For example:
        Let a graph G = (V,E) have...
            V = {0,1,2,3,4,5}
            E = {(0,1), (2,3), (3,4), (4,5), (5,6), (6,7), (7,2)
    With the current graph, our algorithm would remove the leaf node '2' and its associated parent '1' and edges '(1,2)'. However, after this step the algorithm will be unable to identify a new leaf node. Therefore, the edges will never be NULL and our algorithm will be stuck in an infinite while loop. Basically, for vertices 2->7, none of the nodes will have a degree of 1, therefore never being removed / declared as a leaf node. This means the while loop will run infinitely and not gather the 4 matchings.