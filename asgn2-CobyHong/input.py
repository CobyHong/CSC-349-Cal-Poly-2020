import sys
from singleton import *

#Convert shit in file to list bro
file = open(sys.argv[1], "r")
content = file.readlines()
list1 = content[0].split(',')
for i in range(0, len(list1)):
    list1[i] = int(list1[i])

print(singleton(list1))