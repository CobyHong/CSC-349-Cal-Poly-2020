# Pseudo Code for Part 1:

```python
singleton(A <- {a1, ..., an})
    let last_index = length of array minus 1
    let a_mid = (n//2)

    if last_index is 0:
        return a1
    else:
        if a_mid is even:
            if(a_mid == a_mid+1):
                return singleton({a_mid+2, ..., an})
            else:
                return singleton({a1, ..., a_mid+1})
        if a_mid is odd:
            if(a_mid == a_mid-1):
                return singleton({a_mid+1, ..., an})
            else:
                return singleton({a1, ..., a_mid})
```
# Part 1 Proof:

Thereom:
Prove singleton function is correct.

Lemma:
If the sorted sequence of integers "A" contains one and only one unique element and the other elements are all duplicated once. Therefore, singleton funciton returns the one unique element.

Basis Step:
let n = 1. This means A = {a1}. Because a1 is the singleton, singleton function correctly returns a1.

Inductive Hypothesis:
For 1 <= n <= k, if "A" is a sorted sequence of integers containing only one unique element and the other elements are duplicated once, then singleton function returns the one unique element.

Inductive Step:
let n = k + 1
Since k >= 1 and n >= 2, there exist two possibilities:
    -If a_mid is even and a_mid == a_mid+1:
        it must be the case that the singleton is in portion {a_mid, ..., an}
    -If a_mid is even and a_mid != a_mid+1:
        it must be the case that the singleton is in portion {a1, ..., a_mid}
    -If a_mid is odd and a_mid == a_mid-1:
        it must be the case that the singleton is in portion {a_mid, ..., an}
    If a_mid is odd and a_mid != a_mid-1:
        it must be the case that the singleton is in portion {a1, ..., a_mid}
    Noting that all (n/2) size and less than or equal to "k".

By the inductive hypothesis, we prove the singleton funciton correctly returns the singleton element from sorted integer sequence "A".

# Time Complexity:

T(n) = 1 * T(n/2) * O(n)
a = 1, b = 2, d = 0
d = logb(a) --> T(n) = O(n^dlog(n))

Therefore: T(n) = O(logn)


