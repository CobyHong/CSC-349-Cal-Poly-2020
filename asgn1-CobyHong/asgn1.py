import sys
import time
from sorts import *

#Convert shit in file to list bro
file = open(sys.argv[1], "r")
content = file.readlines()
list1 = content[0].split(',')
for i in range(0, len(list1)):
    list1[i] = int(list1[i])
list2 = list1.copy()
list3 = list1.copy()

#PrintList
def printList(myList):
    x = len(myList)
    for i in range(len(myList)-1):
        print(myList[i], end = ", ")
    print(myList[x-1])

initTime = time.time()
selectionSort(list1)
endTime = time.time()
time1 = (endTime - initTime)*1000
print("%s (%.2f ms): " %("Selection Sort", time1), end = '')
printList(list1)

initTime = time.time()
insertionSort(list2)
endTime = time.time()
time2 = (endTime - initTime)*1000
print("%s (%.2f ms): " %("Insertion Sort", time2), end = '')
printList(list2)

initTime = time.time()
mergeSort(list3)
endTime = time.time()
time3 = (endTime - initTime)*1000
print("%s %4s(%.2f ms): " %("Merge Sort", " ", time3), end = '')
printList(list3)