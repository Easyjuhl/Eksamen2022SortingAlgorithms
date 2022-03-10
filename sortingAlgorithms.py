from icecream import ic
from math import sqrt

testlist = [54,32,87,69,420,13,56,34,12,9,42]

def linearSearch(list, search):
    counter = 0
    for i in list:
        if i == search:
            break
        counter += 1
    
    return counter

def binarySearch(list, search):
    pos = int((len(list)/2))
    overallPos = pos
    sortedList = sorted(list)
    while True:
        ic(pos)
        ic(sortedList)

        if sortedList[pos] == search:
            return overallPos
        elif sortedList[pos] < search:
            for i in range(pos):
                sortedList.remove(sortedList[0])
            pos = int(len(sortedList)/2)
            overallPos += pos
        elif sortedList[pos] > search:
            for i in range(pos, len(sortedList)):
                sortedList.remove(sortedList[pos])
            pos = int(len(sortedList)/2)
            overallPos -= pos

def jumpSearch(list, search):
    jump = int(sqrt(len(list)))


print(linearSearch(testlist, 9))
print(binarySearch(testlist, 9))