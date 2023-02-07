import collections
from itertools import combinations
from partsManager import *
import random
import itertools
import threading
import time
import csv

def T1():
    myList = {"joehn", "marry", "john", "james"}
    if len(myList) == len(set(myList)):
        print("There are duplicates")
    else:
        print("There are no duplicates")

def T2():
    listOfElems = ["john", "marry", "john", "james"]
    newElements = list()
    for elem in listOfElems:
        if elem in newElements:
            return True
        else:
            newElements.append(elem)

    return False

def T3():
    myList = [1, 2, 3, 4, 5]
    listComb = []
    for item in combinations(myList, 3):
        listComb.append(item)

    print("{} ==> {}".format(myList, listComb))

def T4():
    myList = [1,4,8,7,2,3,1,4,1,1,4,6,8]
    # Kolik duplikatu se muze vyskytovat (numBer = 2, max 3 stejne elementy)
    numBer = 1
    duplicatesList = []
    duplicat = False
    for item in myList:
        if myList.count(item) > numBer:
            duplicat = True
            duplicatesList.append(item)

    if duplicat:
        print("myList contains a duplicat")
        print(duplicatesList)
    else:
        print("myList does not contain a duplicat")

    newListD = []

    for item in duplicatesList:
        if item not in newListD:
            newListD.append(item)

    tempAllDuplicates = {}

    for item in newListD:
        #tempAllDuplicates.append({item:myList.count(item)})
        tempAllDuplicates[item]=myList.count(item)
        print('{} is {} times in myList'.format(item, myList.count(item)))

    print(tempAllDuplicates)

def findElementXTimes(myList, numBer):
    # Kolik duplikatu se muze vyskytovat (numBer = 2, max 3 stejne elementy)
    #numBer = 1
    duplicatesList = []
    duplicat = False
    for item in myList:
        if myList.count(item) > numBer:
            duplicat = True
            duplicatesList.append(item)

    if duplicat:
        print("Parts contains a duplicat")
        print(duplicatesList)
    else:
        print("Parts does not contain a duplicat")

    newListD = []

    for item in duplicatesList:
        if item not in newListD:
            newListD.append(item)

    tempAllDuplicates = {}

    for item in newListD:
        tempAllDuplicates[item]=myList.count(item)
        print('{} is {} times in myList'.format(item, myList.count(item)))
        duplicateLocated = True

    print(tempAllDuplicates)
    return duplicat

def T5():
    myList = ['DarkBG', 'PinkB', 'PurpleHL', 'GrayOL', 'YellowL', 'LightBG', 'PinkB', 'PinkHL', 'GrayOL', 'WhiteL', 'DarkBG', 'PinkB', 'YellowHL', 'RedOL', 'YellowL', 'DarkBG', 'PinkB', 'WhiteHL', 'RedOL', 'GreenL', 'LightBG', 'PinkB', 'YellowHL', 'RedOL', 'WhiteL', 'DarkBG', 'BlueB', 'PurpleHL', 'RedOL', 'WhiteL', 'DarkBG', 'GreenB', 'RainbowHL', 'RedOL', 'WhiteL', 'DarkBG', 'GreenB', 'PinkHL', 'RedOL', 'YellowL', 'DarkBG', 'PinkB', 'PinkHL', 'RedOL', 'WhiteL', 'LightBG', 'LightBlueB', 'PurpleHL', 'RedOL', 'GreenL', 'MidBG', 'PinkB', 'WhiteHL', 'RedOL', 'WhiteL', 'DarkBG', 'GreenB', 'WhiteHL', 'GrayOL', 'WhiteL', 'MidBG', 'PinkB', 'RainbowHL', 'RedOL', 'YellowL', 'LightBG', 'PinkB', 'WhiteHL', 'GrayOL', 'YellowL', 'LightBG', 'LightBlueB', 'YellowHL', 'GrayOL', 'YellowL', 'DarkBG', 'PinkB', 'RainbowHL', 'WhiteOL', 'WhiteL', 'DarkBG', 'GreenB', 'YellowHL', 'BlueOL', 'YellowL', 'DarkBG', 'WhiteB', 'PurpleHL', 'WhiteOL', 'WhiteL', 'DarkBG', 'RainbowB', 'PurpleHL', 'BlueOL', 'GreenL', 'MidBG', 'GreenB', 'PurpleHL', 'RedOL', 'WhiteL']
    print(findElementXTimes(myList, 2))

def T6():
    print(len(backgroundNames))

def T7():
    numberOfSomething = 3
    for i in range(numberOfSomething):
        print(i)
        numberOfSomething+=1

def T8():
    myList = [0, 0, 0, 0, 0]
    myMaxList = [3, 6, 5, 4, 3]

    def addOneToList():
        global myList

        if myList[0] < len(myMaxList[0]):
                myList[0] += 1
        else:
            myList[0] = 0
            if myList[1] < len(myMaxList[1]):
                myList[1] += 1
            else:
                myList[1] = 0
                if myList[2] < len(myMaxList[2]):
                    myList[2] += 1
                else:
                    # ...
                    pass

    for r in range(20):
        print(myList)
        addOneToList()

    #[0, 0, 0, 0, 0]
    #[1, 0, 0, 0, 0]
    #[2, 0, 0, 0, 0]
    #[0, 1, 0, 0, 0]
    #[1, 1, 0, 0, 0]
    #[2, 1, 0, 0, 0]
    #[0, 2, 0, 0, 0]
    #...
    pass

def T9():
    allLayersMax = [3, 6, 5, 4, 3]
    ranges = [range(1, n+1) for n in allLayersMax]

    someList = []
    for v in itertools.product(*ranges):
        someList.append(list(v))
        print(str(list(v)))

    #print(someList)

def T10():
    def findDuplicates(listOfElems):
        newElements = list()
        for elem in listOfElems:
            if elem in newElements:
                return True
            else:
                newElements.append(elem)

        return False

    myList = ["2", "3", "5s", "5", "4"]
    myBool = findDuplicates(myList)

    print(myBool)

name = ""
def T11():
    name = "john"
    print(name)

def T12():
    myList = ["L1T2","L2T1","L3T1","L4T2","L5T2","L6T1"]
    listComb = []
    for item in combinations(myList, 3):
        listComb.append(item)

    for item in listComb:
        print("{},{},{}".format(item[0], item[1], item[2]))
    print("\n\n\n")

    f = open("/home/martin/Desktop/pythonShit/AxieInfinity/NFTImgGenerator14/calculator/allAttributeCombinations.txt", "r")
    lines = f.readlines()
    for line in lines:
        print(line.replace("\n", ""))

    print("\n\n\n")

    for line in lines:
        for comb in listComb:
            if line.replace("\n", "") == comb:
                print(line)

def T13():
    numbr = 514.2842
    print(round(numbr, 2))

def T14():
    for i in range(9):
        someAllLayersMax = []
        for numbr in range(i+2):
            someAllLayersMax.append(5)
        print(someAllLayersMax)
        print(len(someAllLayersMax))

number = 0
def T15():
    def countTo(xxx):
        #global number
        number = 0
        for i in range(xxx):
            time.sleep(0.5)
            number += 1
        print(number)
    countTo(2)
    countTo(3)

    t1 = threading.Thread(target=countTo, args=(5, ))
    t2 = threading.Thread(target=countTo, args=(5, ))
    t3 = threading.Thread(target=countTo, args=(5, ))
    t4 = threading.Thread(target=countTo, args=(5, ))
    t1.start()
    t2.start()
    t3.start()
    t4.start()

def T16():
    for i in range(1):
        print("ss")

def T17():
    myVariable = (300, 300)
    print(type(myVariable))

def T18():
    p = r"/home/martin/Desktop/pythonShit/AxieInfinity/NFTImgGenerator14/Jsons/"
    p = r"c:\Windows\System32"
    s = 'dd'
    if "\\" in s:
        if s.split('\\')[-1] == '':
            last_word = s.split('\\')[-2]
        else:
            last_word = s.split('\\')[-1]
    elif "/" in s:
        if s.split('/')[-1] == '':
            last_word = s.split('/')[-2]
        else:
            last_word = s.split('/')[-1]
    else:
        print("path {} invalid".format(s))
        exit()

    print(last_word)

def T19():
    myList = [["a"], ["b"], ["c"], ["d"], ["e"]]
    myWeights = [1.49, 1.25, 2, 4, 2]

    Z = [x for _, x in sorted(zip(myWeights, myList))]
    print(Z)

def T20():
    createdCsv = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator14\created.csv"
    with open(createdCsv) as file:
        reader = csv.reader(file)
        createdCsvData = []
        for row in reader:
            createdCsvData.append(row)
    newCreatedCsvData = [list( map(int,i) ) for i in createdCsvData]
    zipedCreatedCsvData = list(zip(*newCreatedCsvData))
    print(zipedCreatedCsvData)

def T21():
    mat = [[1,2,3], [4,5,6]]
    trans_mat = tuple(zip(*mat))
    print(trans_mat)

T20()
#print(name)
