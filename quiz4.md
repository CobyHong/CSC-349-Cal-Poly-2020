# Coby Hong
# CSC-349
# Quiz #4

# Question 1:

# (A):

```Python

Problem 0:
    if either string is empty, then do:
        if "string1" is empty:
            return length of "string2" to be our number of operations.
        if "string2" is empty:
            return length of "string1" to be out number of operations.

Problem 1:
    if last characters of the 2 strings are the same, then do:
        Ignore and continue onto rest of lengths for strings m-1 and n-1.

Problem 2:
    If last characters of the 2 strings are NOT the same, then do:
        Then we perform the following operations:
                -insert: get table position of "string1" m-0, "string2" n-1. #up.
                -delete: get table position of "string1" m-1, "string2" n-0. #left.
            set our current table position equal to the min(insert, delete).

```

# (B):

```Python

def levenshtein(string1 <- {x1, ..., xn}):
Input: A string.
Output: the minimum number of operations needed to reverse the string.

    let string2 be string1.reverse() == string1[::-1]
    let m be the length of string1.
    let n be the length of string2.

    let "table" be a table of dimensions n+1 by m+1.

    for i in range(m+1):
        for j in range(n+1):

            if string1 is empty, then do:
                let current table position[i][j] be j.
            
            else if string2 is empty, then do:
                let current table position[i][j] be i.

            else if current last characters of strings are equivalent, then do:
                Ignore and continue on rest of characters / table position[i-1][j-1].
            
            else:
                let current table position[i][j] be 1 + ...
                    minimum of...
                        -inserted character / table position[i][j-1].
                        -deleted character / table position[i-1][j-1].
            
    return the corner score value of our table[m,n]

```

# (C):

0: [0 1 2 3 4 5 6 7 8]
1: [1 0 1 2 3 4 5 6 7]
2: [2 1 0 1 2 3 4 5 6] 
3: [3 2 1 2 3 4 3 4 5] 
4: [4 3 2 1 2 3 4 5 6] 
5: [5 4 3 2 1 2 3 4 5] 
6: [6 5 4 3 2 1 2 3 4] 
7: [7 6 5 4 3 2 3 2 3] 
8: [8 7 6 5 4 3 4 3 2] 

# (D):

() Time Complexity <- O(n*n) <- O(n^2)
() Reason: This complexity comes from the fact that both strings (start, destination) are the same lengths n. It takes n*n time to contruct our table once and traversal based on the number of elements. Basically, we need n*n space in our table.