# Coby Hong
# CSC 349
# Quiz 5

# Question 1

# (A)

Given an undirected, unweighted Graph G, determine if the graph coloring is proper if using 'k' colors and if adjacent vertices have different colors.
If there is no k-1 solution then we have the minimal solution. If there exist a k-1 solution, then we do not have the minimal solution.

# (B)

The vertex coloring problem is NP since you have to check if all the
neighbors of the current vertex are different colors. After, you count
the total of different colors. The algorithm in polynomial time since just
have to see if whether or not it is 'k' colors. Does not have to find the 
minimum solution, just has to check for 'k' colors. 
Basically, can just compare endpoint of every edge in linear time.

# (C)

We can show that Vertex Coloring problem is also NP-Hard, thereby NP-Complete by
using k=3 to instantiate a 3-Coloring graph. With a 3-Coloring graph, we can than
convert into the NP-Hard problem, 3SAT. This still holding true to k-coloring.
k-coloring being NP-Complete by how we check the coloring to show that 3SAT is less than
or equal to 3-Coloring. 

We will produce 3 nodes of value: Base, Color1, Color2.
Basically having a base and two other connected nodes that we will identify by Ni and Ni2.
In every 3-coloring, the values / coloring of Ni and Ni2 cannot be the same value (Color1, Color2).

We can determine 3-colorability by at the given vertex serving as our base by these claims:
    -If Ni, Ni2, and Nin (some other connection to base) is same color:
        -then we are not 3-colorable since 2 of the vertices connected to the base share in color.
    -If Ni, Ni2, and Nin (some other connection to base) are not all the same color:
        -then this aspect of the graph is 3-colorable as distinction of at least 2 colors in the connected nodes exist.
    -In short, we can determine 3-colorability by how at least one of the three nodes is colored differently.

By proving Graph Coloring in k-colors with 3SAT, which is a NP-Hard problem, we have proven that our own problem is
as well NP-Hard and therefore is also NP-Complete.


# Question 2

That means this NP-Complete problem would be solvable in polynomial time.