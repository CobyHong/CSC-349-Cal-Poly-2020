# Pseudo Code:

```Python
-forward_graph <- {a1 : {b1, ..., bn}, ... an}
-reverse_graph <- transpose(forward_graph)

def kosajaru(forward_graph, reverse_graph):
  let stack be an empty array [].
  let vertex_length = len(forward_graph)

  let visited be an array of "False" boolean values length of vertex_length.
  
  for vertex in forward_graph do:
    if current vertex is "False", then do:
      filler_explore(forward_graph, vertex, visited, stack)

  reset visited array back to "False" boolean values.
  let component_result be an empty array.

  while the stack is not empty do:
    let 'item' be popped vertex from stack[].
    if visited[] at 'item' index is "False", then do:
      let component_list be an empty array.
      util_explore(reverse_graph, 'item', visited, component_list)
      component_list.sort()
      add component_list to component_result.
  return component_result
```


```Python
def filler_explore(forward_graph, vertex, visited, stack):
  let visited value of vertex be "True".

  for vertex in forward_graph[vertex] do:
    if visited[] at vertex index is "False", then do:
      filler_explore(forward_graph, vertex, visited, stack)
  add vertex to stack.
```


```Python
def util_explore(reverse_graph, vertex, visited, component_list):
  let visited value of vertex be "True".
  add vertex to component_list.

  for vertex in reverse_graph[vertex] do:
    if visited[] at vertex index is "False", then do:
      util_explore(forward_graph, vertex, visited, component_list)
```
