from turtle import end_fill
from PIL import Image 
from IPython.display import display 
import random
import json
import os
import shutil
from itertools import combinations
import collections
import csv
import copy
import time
import itertools
from tkinter import *
from threading import Thread


allImages = []
allAttributeCombinations = []
allParts = []
tempAllParts = []
thisAttributes = []
thisAttributeCombinations = []
tempAllAttributeCombinations = []
numOfImages = 0
numOfDuplicates = 0
allCombinations = []
layerOne = []
layerTwo = []
layerThree = []
layerFour = []
layerFive = []
layerSix = []
layerSeven = []
layerEight = []
layerNine = []
layerTen = []
allLayers = [layerOne, layerTwo, layerThree, layerFour, layerFive, layerSix, layerSeven, layerEight, layerNine, layerTen]
allLayerNames = ["layerOne", "layerTwo", "layerThree", "layerFour", "layerFive", "layerSix", "layerSeven", "layerEight", "layerNine", "layerTen"]

def resetVariables():
    global allImages, allAttributeCombinations, allParts, allPartsCount, numOfImages, numOfDuplicates, allCombinations

    allImages = []
    allAttributeCombinations = []
    allParts = []
    numOfImages = 0
    numOfDuplicates = 0
    allCombinations = []

def findDuplicates(listOfElems):
    newElements = list()
    for elem in listOfElems:
        if elem in newElements:
            return True
        else:
            newElements.append(elem)  
    return False

def prepareLists(thisNumOfLayers, thisAllLayersMax):
    global layerOne, layerTwo, layerThree, layerFour, layerFive, layerSix, layerSeven, layerEight, layerNine, layerTen

    #for e in allLayers:
    #    e = []
    
    layerOne = []
    layerTwo = []
    layerThree = []
    layerFour = []
    layerFive = []
    layerSix = []
    layerSeven = []
    layerEight = []
    layerNine = []
    layerTen = []

    for i in range(thisNumOfLayers):
        for e in range(thisAllLayersMax[i]):
            allLayers[i].append("L"+str(i+1)+"T"+str(e+1))

    for i in range(thisNumOfLayers):
        #print("{} = {}".format(allLayerNames[i], allLayers[i]))
        pass

def createNewImage(thisChosenTraits, thisNumOfLayers, thisCombinationsLength):
    global allImages, allAttributeCombinations, allParts

    newImage = {}
    tempAllAttributeCombinations = []
    tempAllParts = []
    thisAttributes = []

    for i in range(thisNumOfLayers):
        newImage [allLayerNames[i]] = allLayers[i][thisChosenTraits[i]-1]
        
    #print(newImage)

    thisAttributes = list(newImage.values())

    for item in allAttributeCombinations:
        tempAllAttributeCombinations.append(item)

    for item in combinations(thisAttributes, thisCombinationsLength):
        tempAllAttributeCombinations.append(item)
    
    for item in allParts:
        tempAllParts.append(item)

    for item in newImage:
        tempAllParts.append(newImage[item])

    thisDuplicate = findDuplicates(tempAllAttributeCombinations)

    if thisDuplicate:
        return 'duplicate'
    
    for item in combinations(thisAttributes, thisCombinationsLength):
        allAttributeCombinations.append(item)

    for item in newImage:
        allParts.append(newImage[item])
    
    if newImage in allImages:
        return 'duplicate'
    else:
        return newImage

def createAllImages(thisNumOfLayers, thisAllLayersMax, thisCombinationsLength):
    global allImages, allAttributeCombinations, newAttributes, numOfAttempts, newAttributesCollection, numOfImages, combinationsLength, numOfDuplicates, allCombinations, listOfAllPossibilities, allRanges

    chosenTraits = []
    for i in range(thisNumOfLayers):
        chosenTraits.append(0)

    allRanges = [range(1, n+1) for n in thisAllLayersMax[::-1]]

    listOfAllPossibilities = []
    for v in itertools.product(*allRanges):
        listOfAllPossibilities.append(list(v[::-1]))

    newTraitImage = None
    for p in listOfAllPossibilities: 
        #print(p)
        #exit()
        newTraitImage = createNewImage(p, len(thisAllLayersMax), thisCombinationsLength)

        if newTraitImage != 'duplicate':
            allImages.append(newTraitImage)
            numOfImages += 1
            allCombinations.append(p.copy())
 
        elif newTraitImage == 'duplicate':
            numOfDuplicates += 1
    
    return numOfImages, numOfDuplicates

animation = "|/-\\"
idx = 0
playAnim = True

def loadingAnim():
    global idx
    while playAnim:
        print(animation[idx % len(animation)], end="\r")
        idx += 1
        time.sleep(0.1)
    return


numOfLayers = 5
allLayersMax = [3, 6, 5, 4, 3]
combinationsLength = 3
prepareLists(numOfLayers, allLayersMax)
#for i in range(3):
#    numOfImages, numOfDuplicates = createAllImages(numOfLayers, allLayersMax, i+2)
#    print("numOfImages:"+str(numOfImages))
#    print("numOfDuplicates:"+str(numOfDuplicates))

animThread = Thread(target=loadingAnim)
animThread.start()

someAllLayersMax = [3, 3, 3, 3, 3, 3]
ranges = [range(2, n+1) for n in someAllLayersMax[::-1]]

someList = []
for v in itertools.product(*ranges):
    someList.append(list(v))

#print(someList)


for layer in someList:
    numOfLayers = len(layer)
    prepareLists(numOfLayers, layer)
    numOfImages, numOfDuplicates = createAllImages(numOfLayers, layer, combinationsLength)
    print("layer:"+str(layer))
    print("combinationsLength:"+str(combinationsLength))
    print("numOfImages:"+str(numOfImages))
    print("numOfDuplicates:"+str(numOfDuplicates))

    playAnim = False
    exit()

playAnim = False


#t1 = Thread(target=createAllImages, args=(numOfLayers, allLayersMax, combinationsLength, ))
#t1.start()

#numOfImagest1, numOfDuplicatest1 = t1.join()
#print("numOfImages:"+str(numOfImagest1))
#print("numOfDuplicates:"+str(numOfDuplicatest1))

