# Pseudo Code:

```Python
-graph <- {a1 : {b1, ..., bn}, ... an}

Input: 
a dictionary consisting of edges.
Output: 
a dictionary where the keys are the degrees and the values are the vertexes associated with those degrees.

def kcores(graph):
  let k be 1.
  let kcores be an empty dictionary {}.
  let remove_list be an empty array [].

  let v_d be an array of tuples:
    #EX: [(0,1) , ... ]
    -first value being the vertex. #0 would be vertex.
    -second value the level of degree. #1 would be degree.
  
  while v_d is not empty, do:
    let head_v_d be the first instance in v_d.

    if degree of head_v_d is less than or equal to k, do:
      pop head_v_d from v_d and append to remove_list.
      remove vertex of head_v_d from our graph.
      let v_d be v_d but based on new graph.
    else, do:
      let kcores[k] be a sorted array of vertexes associated with that degree number/value.
      increment k by 1.
      let remove_list be an empty array[].

  if remove_list is not empty, do:
    append leftover degrees that do not lie in similar subset to kcores[k].
    sort kcores[k]
  
  for key in kcores, do:
    merge lower level kcore vertexes with current key / k level.
  
  return kcores.
```

# Brief Description:

This algorithm makes the locally optimal choice of always picking vertices based off the lowest degree value. Since we always grab the lowest degree value from our list, the algorithm leads to the globally optimal choice because the vertices that will be remaining will be the ones associated with the max kcore value of the graph.