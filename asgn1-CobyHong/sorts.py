import sys
import time

#SelectionSort
def selectionSort(list1):
    for i in range(len(list1)):
        minIDX = i
        for j in range(i+1, len(list1)):
            if list1[minIDX] > list1[j]:
                minIDX = j
        temp = list1[i]
        list1[i] = list1[minIDX]
        list1[minIDX] = temp

#InsertionSort
def insertionSort(list2):
    for i in range(1, len(list2)):
        currVal = list2[i]
        pos = i
        while pos > 0 and list2[pos-1] > currVal:
            list2[pos] = list2[pos-1]
            pos = pos-1
        list2[pos] = currVal

#MergeSort
def mergeSort(list3):
    if len(list3) > 1:
        mid = len(list3) // 2
        left = list3[:mid]
        right = list3[mid:]
        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              list3[k] = left[i]
              i += 1
            else:
                list3[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            list3[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list3[k]=right[j]
            j += 1
            k += 1