import itertools
from itertools import combinations
import csv

from partsManager import *

allImages = []
allAttributeCombinations = []
allParts = []
allPartsCount = {}
tempAllParts = []
thisAttributes = []
thisAttributeCombinations = []
tempAllAttributeCombinations = []
cobinationsLength = 3
allTraits = []

csvPath = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator11\created.csv"

def findDuplicates(listOfElems):
    newElements = list()
    for elem in listOfElems:
        if elem in newElements:
            return True, elem
        else:
            newElements.append(elem)

    return False, None

cobinationsLength += 1

def findElementXTimes(myList):

    duplicatesList = []
    for item in myList:
        duplicatesList.append(item)

    newListD = []

    for item in duplicatesList:
        if item not in newListD:
            newListD.append(item)

    tempAllDuplicates = {}

    for item in newListD:
        tempAllDuplicates[item]=myList.count(item)

    fullList = nullParts

    for item in tempAllDuplicates:
        fullList[item] = tempAllDuplicates[item]


    return fullList



def createNewImage(chosenTraits):
    global allImages, allAttributeCombinations, newAttributes, newAttributesCollection, tempAllAttributeCombinations, allParts, tempAllParts, allTraits

    newImage = {}

    newImage ["Background"] = backgroundNames[chosenTraits[0]-1]
    newImage ["Body"] = bodyNames[chosenTraits[1]-1]
    newImage ["Highlight"] = highlightNames[chosenTraits[2]-1]
    newImage ["Outline"] = outlineNames[chosenTraits[3]-1]
    newImage ["Light"] = lightNames[chosenTraits[4]-1]


    thisAttributes = list(newImage.values())

    thisAttributeCombinations = []
    tempAllAttributeCombinations = []
    tempAllParts = []

    for item in allAttributeCombinations:
        tempAllAttributeCombinations.append(item)

    for item in combinations(thisAttributes, cobinationsLength):
        thisAttributeCombinations.append(item)
        tempAllAttributeCombinations.append(item)

    for item in allParts:
        tempAllParts.append(item)

    for item in newImage:
        tempAllParts.append(newImage[item])

    thisDuplicate, thisDuplicateItem = findDuplicates(tempAllAttributeCombinations)

    allPartsCount = findElementXTimes(tempAllParts)

    for item in maxParts:
        if maxParts[item] != 0:
            if allPartsCount[item] > maxParts[item]:
                thisDuplicate = True


    if thisDuplicate:
        return 'duplicate'

    for item in combinations(thisAttributes, cobinationsLength):
        allAttributeCombinations.append(item)

    for item in newImage:
        allParts.append(newImage[item])

    if newImage in allImages:
        print(newImage)
        print("A whole image is repeating. How? IDK")
        return 'duplicate'
    else:
        print("Img num: "+str(len(allImages))+"; chosenTraits: "+str(chosenTraits))
        # allTraits.append(["L1T{}".format(chosenTraits[0]), "L2T{}".format(chosenTraits[1]), "L3T{}".format(chosenTraits[2]), "L4T{}".format(chosenTraits[3]), "L5T{}".format(chosenTraits[4])])
        allTraits.append(chosenTraits)
        return newImage



allLayersMax = [len(backgroundNames), len(bodyNames), len(highlightNames), len(outlineNames), len(lightNames)]
ranges = [range(1, n+1) for n in allLayersMax]
someList = []

for v in itertools.product(*ranges):
    someList.append(list(v))

print(str(len(someList)))

for chosenTraits in someList:
    newTraitImage = createNewImage(chosenTraits)

    if newTraitImage != 'error' and newTraitImage != 'duplicate':
        allImages.append(newTraitImage)
    elif newTraitImage == 'duplicate':
        pass
    if newTraitImage == 'error':
        print("An error has occured")
        exit()

def allImagesUnique(listToCheck):
    seen = list()
    return not any(i in seen or seen.append(i) for i in listToCheck)

print("Are all images unique?", allImagesUnique(allImages))

print(allTraits)
header = []
f = open(csvPath, "w", newline='')
writer = csv.writer(f)


# writer.writerow(header)
writer.writerows(allTraits)

f.close()
