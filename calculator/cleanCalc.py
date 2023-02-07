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
import numpy
from helper import *

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

def percentage(part, whole):
  percentage = 100 * float(part)/float(whole)
  return percentage

def prepareLists(thisNumOfLayers, thisAllLayersMax):
    global layerOne, layerTwo, layerThree, layerFour, layerFive, layerSix, layerSeven, layerEight, layerNine, layerTen

    for i in range(thisNumOfLayers):
        allLayers[i] = []

    for i in range(thisNumOfLayers):
        pass
        #print("{} = {}".format(allLayerNames[i], allLayers[i]))


    for i in range(thisNumOfLayers):
        for e in range(thisAllLayersMax[i]):
            allLayers[i].append("L"+str(i+1)+"T"+str(e+1))

    for i in range(thisNumOfLayers):
        pass
        #print("{} = {}".format(allLayerNames[i], allLayers[i]))



def createNewImage(thisChosenTraits, thisNumOfLayers, createNewCombinationsLength):
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

    for item in combinations(thisAttributes, createNewCombinationsLength):
        tempAllAttributeCombinations.append(item)
        #print("item:"+str(item))
    #exit()

    for item in allParts:
        tempAllParts.append(item)

    for item in newImage:
        tempAllParts.append(newImage[item])

    thisDuplicate = findDuplicates(tempAllAttributeCombinations)

    if thisDuplicate:
        return 'duplicate'

    for item in combinations(thisAttributes, createNewCombinationsLength):
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

    #print(listOfAllPossibilities)
    #exit()
    newTraitImage = None
    resetVariables()
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
        else:
            print("error")

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



#for i in range(3):
#    numOfImages, numOfDuplicates = createAllImages(numOfLayers, allLayersMax, i+2)
#    print("numOfImages:"+str(numOfImages))
#    print("numOfDuplicates:"+str(numOfDuplicates))

animThread = Thread(target=loadingAnim)
#animThread.start()

for i in range(1):
    start_time = time.time()
    someAllLayersMax = []
    for numbr in range(5):
        someAllLayersMax.append(6)

    combinationsLength = len(someAllLayersMax)
    combList = []
    for num in range(combinationsLength-1):
        combList.append(num+2)

    combList = [2, 3, 4, 5]
    numOfLayers = len(someAllLayersMax)
    ranges = [range(2, n+1) for n in someAllLayersMax]

    someList = []
    for v in itertools.product(*ranges):
        someList.append(list(v))

    someList = [[3, 6, 5, 4, 3]]

    header = []
    allLines = []

    for i in range(len(someAllLayersMax)):
        header.append(str("L"+str(i+1)))

    header.append("totalComb")

    for item in combList:
        header.append(str("max"+str(item)+"Opak"))

    for item in range(len(combList)):
        header.append(str(item+2)+"/total")

    for layer in someList:
        numOfLayers = len(layer)
        newLineMaxComb = []
        for combNum in combList:
            #print("CombNum:"+str(combNum))
            prepareLists(numOfLayers, layer)
            thisNumOfImages, thisNumOfDuplicates = createAllImages(numOfLayers, layer, combNum)
            #print("layer:"+str(layer)+" combNum:"+str(combNum)+" numOfGoodImages:"+str(thisNumOfImages)+" thisNumOfDuplicates:"+str(thisNumOfDuplicates)+" numOfAllAttempts:"+str(thisNumOfImages+thisNumOfDuplicates))
            #L1	L2	L3	L4	L5	L6	total comb	max 2 opak	max 3 opak	max 4 opak	3/total	4/total
            newLineMaxComb.append(thisNumOfImages)
        newLine = []
        for numbr in layer:
            newLine.append(numbr)
        newLine.append(numpy.prod(layer))

        for item in newLineMaxComb:
            newLine.append(item)

        for item in newLineMaxComb:
            newLine.append(str(round(percentage(item, int(numpy.prod(layer))), 3))+"%")

        allLines.append(newLine)
        print(newLine)
        #print("{} attributes done".format(str(len(someAllLayersMax))))
        #print("combinationsLength:"+str(combinationsLength))
        #print("numOfImages:"+str(numOfImages))
        #print("numOfDuplicates:"+str(numOfDuplicates))
        #print("allAttributeCombinations:"+str(allAttributeCombinations))
        #print(findDuplicates(allAttributeCombinations))

        if False:
            f = open(r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator16\calculator\allImages.csv", "w", newline='')
            writer = csv.writer(f)
            for item in allImages:
                writer.writerow(item.values())
            f.close()

            f = open(r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator16\calculator\allAttributeCombinations.csv", "w", newline='')
            writer = csv.writer(f)
            for item in allAttributeCombinations:
                writer.writerow(item)
            f.close()

            playAnim = False
            exit()
    print("{} attributes done".format(str(len(someAllLayersMax))))
    print("This operation took %s seconds" % (time.time() - start_time))

    nameOfFile = str(len(someAllLayersMax))+"AttributesSomething.csv"
    with open(r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator16\calculator\\"+nameOfFile, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for item in allLines:
            writer.writerow(item)

playAnim = False



#t1 = Thread(target=createAllImages, args=(numOfLayers, allLayersMax, combinationsLength, ))
#t1.start()

#numOfImagest1, numOfDuplicatest1 = t1.join()
#print("numOfImages:"+str(numOfImagest1))
#print("numOfDuplicates:"+str(numOfDuplicatest1))
