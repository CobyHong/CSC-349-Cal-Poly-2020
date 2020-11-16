# Pseudo Code for Part 2:

```python
singleton(A <- {a1, ..., an})
    let a_mid = (n//2)
    let leftHalf = {a1, ..., a_mid}
    let rightHalf = {a_mid, ..., an}

    return merge(singleton(leftHalf), singleton(rightHalf), leftHalf, rightHalf)

merge(left_A, right_A, leftHalf, rightHalf)
    let result = []

    for loop through left_A:
        if (left_A_item is not right_A_first_item):
            result.add(left_A_item)
    
    for loop through right_A:
        if (right_A_item is not left_A_last_item):
            result.add(right_A_item)
    
    return result
```
# Part 2 Proof:

Thereom:
Prove singleton function is correct.

Lemma:
If the sorted sequence of integers "A" contains one and only one unique element and the other elements are all duplicated at least once. Therefore, singleton funciton returns the one unique element.

Basis Step:
let n = 1. This means A = {a1}. Because a1 is the singleton, singleton function correctly returns a1.

Inductive Hypothesis:
For 1 <= n <= k, if "A" is a sorted sequence of integers containing only one unique element and the other elements are duplicated at least once, then singleton function returns the one unique element.

Inductive Step:
let n = k + 1
Since k >= 1 and n >= 2, there exist two possibilities:
    -If an item in the left half is not equal to the first item in the right half:
        then append that item to our result.
    -If an item in the right half is not equal to the first item in the left half:
        then append that item to our result.

Since the function that relates these possibilities is called recursively onto halves of the sequence "A", the output will be correct for size (n//2), (n//4) and so on. This deduction will continue until singleton returns a single item that is unique in the sequence "A" from the left or right half. The two singleton calls will return the single items on the left and right half recursively and merging until resulting in a singular unique item.

By the inductive hypothesis, we prove the singleton function correctly returns the singleton element from the sorted integer sequence "A".


# Time Complexity:

T(n) = 1 * T(n/2) * O(n)
a = 1, b = 2, d = 1
d > logb(a) --> T(n) = O(n^d)

Therefore: T(n) = O(n)


