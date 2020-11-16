```Python

string1 <- {x1, ..., xn}
string2 <- {y1, ..., yn}

def wunsch(string1, string2):
  Input:
    A string labeled "string1", a string labeled "string2".
  Output:
    Highest Scoring Alignment of the two strings.

  Definition:
    Let T(i,j) be the highest scoring alignment between "string1" and "string2".

  Base Cases:
    - T(i,0) = T(i-1,0) + dictionary of '-i'.
    - T(0,j) = T(0,j-1) + dictionary of 'j-'.

  Formula:
    T(i,j) = ...
        - T(i-1, j-1) + score (if xi == yi) '#1'
        - (T(i,j-1) + score, T(i-1,j) + score) (if xi != yi) '#2'
        - max('#1', '#2')

    score:
      - matching
      - mismatch
      - gap

  Solution:
    T(n,m)

```