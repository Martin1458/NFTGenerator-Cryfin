import collections
from itertools import combinations
from partsManager import *
import random

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

T7()