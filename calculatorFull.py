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


# List vsech obrazku (jejich attributu)
allImages = []
# List vsech kombinaci (viz: cobinationsLength)
allAttributeCombinations = []
# List vsech casti ve vsech obrazcich
# Pro max
allParts = []
# Pocet vsech jednotlivych casti
allPartsCount = {}
# List vsech casti ve vsech obrazcich
tempAllParts = []
# 'this' = pred kazdym obrazkem se vynuluje
# Attributy aktualniho obrazku
thisAttributes = []
# Vsechny aktualni kombinace attributu (viz: cobinationsLength)
thisAttributeCombinations = []
# allAttributeCombinations + thisAttributeCombinations 
# pouziva se na zkontrolovani duplikatu predtim nez se kombinace zapisou do allAttributeCombinations
tempAllAttributeCombinations = []
# Pocet aktualnich pokusu
numOfAttempts = 0
# Maximalni pocet pokusu o novy obrazek bez duplikatu (Python Failsafe to zastavi u 1000)
maxAttempts = 3000
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
    global allImages, allAttributeCombinations, allParts, allPartsCount, tempAllParts, thisAttributes, thisAttributeCombinations, tempAllAttributeCombinations, numOfAttempts, maxAttempts, numOfImages, numOfDuplicates, allCombinations
    global layerOne, layerTwo, layerThree, layerFour, layerFive, layerSix, layerSeven, layerEight, layerNine, layerTen, allLayers, allLayerNames
    
    allImages = []
    allAttributeCombinations = []
    allParts = []
    allPartsCount = {}
    tempAllParts = []
    thisAttributes = []
    thisAttributeCombinations = []
    tempAllAttributeCombinations = []
    numOfAttempts = 0
    maxAttempts = 3000
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


# Tato funkce najde duplikaty v dannem listu
# Vraci bool (True = tento list obsahuje duplikaty) a list (kombinace ktera se duplikuje)
def findDuplicates(listOfElems):
    newElements = list()
    for elem in listOfElems:
        if elem in newElements:
            return True, elem
        else:
            newElements.append(elem)  

    return False, None

# Tato funkce vrati pocet kazdeho elementu, kolikrat se opakuje v myList
#def findElementXTimes(myList):
#
#    duplicatesList = []
#    for item in myList:
#        duplicatesList.append(item)
#    
#    newListD = []
#
#    for item in duplicatesList:
#        if item not in newListD:
#            newListD.append(item)
#    
#    tempAllDuplicates = {}
#
#    for item in newListD:
#        tempAllDuplicates[item]=myList.count(item)
#        #print('{} is {} times in all images'.format(item, myList.count(item)))
#    
#    fullList = nullParts
#
#    for item in tempAllDuplicates:
#        fullList[item] = tempAllDuplicates[item]
#
#
#    #print(tempAllDuplicates)
#    return fullList


# Test findDuplicates (pokud funguje napise "john")  
# myList = ["john", "marry", "john", "james"]
# myBool, myDuplicate = findDuplicates(myList)
# print(myDuplicate)

# Tato funkce vygeneruje originalni obrazek
def createNewImage(chosenTraits):
    # global = promenne ktere ma tato funkce pravo menit
    global allImages, allAttributeCombinations, newAttributes, numOfAttempts, newAttributesCollection, tempAllAttributeCombinations, allParts, tempAllParts

    # vytvor/vynuluj list pro vytvoreni noveho ojbrazku
    newImage = {}

    # vyber "Background", "Body", "Highlight", "Outline" a "Light" podle tabulek z partsManager.py
    #newImage ["Background"] = backgroundNames[chosenTraits[0]-1]
    #newImage ["Body"] = bodyNames[chosenTraits[1]-1]
    #newImage ["Highlight"] = highlightNames[chosenTraits[2]-1]
    #newImage ["Outline"] = outlineNames[chosenTraits[3]-1]
    #newImage ["Light"] = lightNames[chosenTraits[4]-1]
    #chosenTraits = [2, 4, 5, 4, 3]
    #print(chosenTraits)
    for i in range(numOfLayers):
        newImage [allLayerNames[i]] = allLayers[i][chosenTraits[i]-1]
        #print(newImage)

    # for item in newImage:
    #     print("{} has choosen {} trait".format(item, newImage[item]))
    # exit()
    # print(type(newImage))

    # nastavi thisAttributes na konkretni nazvy casti tohoto obrazku
    thisAttributes = list(newImage.values())
    # print(thisAttributes)
    # print(type(thisAttributes))

    # vynuluje thisAttributeCombinations a tempAllAttributeCombinations pro hledani duplikatu
    thisAttributeCombinations = []
    tempAllAttributeCombinations = []
    tempAllParts = []

    # prida vsechny predchozi (pokud nejake) kombinace do tempAllAttributeCombinations
    for item in allAttributeCombinations:
        tempAllAttributeCombinations.append(item)

    # 'combinations(x, y)' vytvori list vsech moznych kombinaci 'y' itemu z listu 'x'
    # priklad: [1, 2, 3, 4, 5] ==> [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]
    # prida kombinace do thisAttributeCombinations a tempAllAttributeCombinations
    for item in combinations(thisAttributes, combinationsLength):
        thisAttributeCombinations.append(item)
        tempAllAttributeCombinations.append(item)
    
    # zapise vsechny minule i aktualni traity do tempAllParts, na zkontrolovani pro maximalni pocet jednotlivych traitu
    for item in allParts:
        tempAllParts.append(item)

    for item in newImage:
        tempAllParts.append(newImage[item])

    # s pouzitim funkce findDuplicates najdeme (pokud existuje) duplikat.
    # po tom co funkce findDuplicates najde prvni duplikat tak se vypne.
    # thisDuplicate se nastavi na True pokud tempAllAttributeCombinations obsahuje duplikat
    # thisDuplicateItem se nastavi na ten konkretni duplikat (pouzito hlavne pro testy)
    thisDuplicate, thisDuplicateItem = findDuplicates(tempAllAttributeCombinations)

    # Pomoci funkce findElementXTimes vygeneruje allPartsCount, kam se ulozi pocty jednotlivych traits
    #allPartsCount = findElementXTimes(tempAllParts)

    # Zkontroluje pro kazdou trait zda se jiz nevyskytuje vicekrat nez by mela
    #for item in maxParts:
    #    if maxParts[item] != 0:
    #        if allPartsCount[item] > maxParts[item]:
    #            thisDuplicate = True

    # ukaze duplikat pokud existuje, jinak napise None
    #print(thisDuplicateItem)

    # Zkontroluje pokud se neprekrocil maximalni pocet pokusu pro vytvoreni noveho obrazku bez duplikatu
    # (Nahrazeni defaultinho failsafu)
    #if numOfAttempts > maxAttempts:
    #    print("Num of attemps exceeded")
    #    return "error"

    # pokud se jiz duplikat nasel, funkce createNewImage se restartuje
    if thisDuplicate:
        # prida 1 k poctu pokusu k vytvoreni tohoto obrazku
        numOfAttempts += 1
        return 'duplicate'
    
    # Ted kdyz uz  jsme se zbavili duplikatu, zapiseme aktualni kombinace do allAttributeCombinations
    # (Aby jsme mohli zkontrolovat dalsi obrazky)
    for item in combinations(thisAttributes, combinationsLength):
        allAttributeCombinations.append(item)

    # Zapise nove 
    for item in newImage:
        allParts.append(newImage[item])
    
    # Zkontroluje zda obrazek jiz neexistuje
    if newImage in allImages:
        #print(newImage)
        #print("A whole image is repeating. How? IDK")
        numOfAttempts += 1
        return 'duplicate'
    else:
        numOfAttempts = 0
        # Ted uz by nemeli existovat zadne duplikaty, vratime tedy vybrane attributy
        return newImage


# Tato funkce pomoci createNewImage vytvori danny pocet obrzku a projistotu je znovu zkontroluje pro duplikaty
def createAllImages():
    global allImages, allAttributeCombinations, newAttributes, numOfAttempts, newAttributesCollection, numOfImages, combinationsLength, numOfDuplicates, allCombinations, listOfAllPossibilities, allRanges

    chosenTraits = []
    for i in range(numOfLayers):
        chosenTraits.append(0)

    allRanges = [range(n+1) for n in allLayersMax[::-1]]

    listOfAllPossibilities = []
    for v in itertools.product(*allRanges):
        listOfAllPossibilities.append(list(v[::-1]))
        #print(type(v[::-1]))
        

    #print(listOfAllPossibilities)
    #exit()

    newTraitImage = None
    possibility = 0
    while newTraitImage != 'errror': 

        newTraitImage = createNewImage(listOfAllPossibilities[possibility])
        #newTraitImage = 'duplicate'
        # pokud createNewImage nevrati error, zapise obrazek do allImages, jinak ukonci script.
        if newTraitImage != 'error' and newTraitImage != 'duplicate':
            allImages.append(newTraitImage)
            numOfImages += 1
            allCombinations.append(listOfAllPossibilities[possibility].copy())
            #print(listOfAllPossibilities[possibility])
            #print(allCombinations)
            

            #Add one
            possibility += 1

        elif newTraitImage == 'duplicate':
            numOfDuplicates += 1

            #Add one
            possibility += 1
                        
            #print(listOfAllPossibilities[possibility])


        if listOfAllPossibilities[possibility] == allLayersMax:
            newTraitImage = 'errror'
            print("All combinations tried")

        if newTraitImage == 'error':
            print("An error has occured")
            exit()
    #print("\n")
    #print(allCombinations)
    #print("\n")

def prepareLists():
    global layerOne, layerTwo, layerThree, layerFour, layerFive, layerSix, layerSeven, layerEight, layerNine, layerTen

    #print(allLayers)

    for e in allLayers:
        e = []

    #print(allLayers)

    for i in range(numOfLayers):
        for e in range(allLayersMax[i]):
            allLayers[i].append("L"+str(i+1)+"T"+str(e+1))

    #print(allLayers)
    #print(layerOne)
    #exit()

    for i in range(numOfLayers):
        print("{} = {}".format(allLayerNames[i], allLayers[i]))


def calculateLayer(combinationsLength):

    prepareLists()

    # Volani hlavni funkce pro vytvoreni obrazku
    createAllImages()

    #print(allCombinations)
    #format allCombinations
    newStrCombinations = []
    for oneCombination in allCombinations:
        # combination = [1, 0, 1, 1, 2]
        newCombination = []
        numOfTrait = 1
        for trait in oneCombination:
            # numOfTrait+1 protoze python vidi 0 jako prvni trait
            newTrait = "L" + str(numOfTrait) + "T" + str(trait+1)
            newCombination.append(newTrait)
            numOfTrait += 1
        
        #newCombination = [str(x) + "L" for x in oneCombination]
        newStrCombinations.append(newCombination)

    #print(newStrCombinations)
    header = ["Var1", "Var2", "Var3", "Var4", "Var5"]

    if combinationsLength == 2:
        nameOfCsv = "twoComabinations.csv"
    elif combinationsLength == 3:
        nameOfCsv = "threeComabinations.csv"
    elif combinationsLength == 4:
        nameOfCsv = "fourComabinations.csv"
    elif combinationsLength == 5:
        nameOfCsv = "fiveComabinations.csv"
    elif combinationsLength == 6:
        nameOfCsv = "sixComabinations.csv"
    elif combinationsLength == 7:
        nameOfCsv = "sevenComabinations.csv"
    elif combinationsLength == 8:
        nameOfCsv = "eightComabinations.csv"
    elif combinationsLength == 9:
        nameOfCsv = "nineComabinations.csv"
    elif combinationsLength == 10:
        nameOfCsv = "tenComabinations.csv"

    f = open(nameOfCsv, 'w')
    writer = csv.writer(f)
    writer.writerow(header)

    for item in newStrCombinations:
        writer.writerow(item)

    f.close()
    print("combinationsLength: {} numOfImages: {} numOfDuplicates: {} numOfImages+numOfDuplicates: {}".format(combinationsLength, numOfImages, numOfDuplicates, numOfImages+numOfDuplicates))
    resetVariables()


def calculateIt(combinationsLengthX, numOfLayersX, allLayersMaxX):

    start_time = time.time()

    # Pocet attributu co se nesmi opakovat
    combinationsLength = combinationsLengthX

    numOfLayers = numOfLayersX
    allLayersMax = allLayersMaxX
    
    if numOfLayers != len(allLayersMax):
        print("U stupid?")
        exit()

    calculateLayer(combinationsLength)

    print("This operation took %s seconds" % (time.time() - start_time))

#GUI
window = Tk()
window.title("myCalculator")
window.geometry('800x500')

window.columnconfigure(0, weight=2)
window.rowconfigure(0, weight=2)
window.columnconfigure(1, weight=1)
window.rowconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=1)
window.rowconfigure(7, weight=1)
window.rowconfigure(8, weight=1)
window.rowconfigure(9, weight=1)
window.rowconfigure(10, weight=1)
window.rowconfigure(11, weight=1)
window.rowconfigure(12, weight=1)
window.rowconfigure(13, weight=1)
window.rowconfigure(14, weight=1)
window.rowconfigure(15, weight=1)

title = Label(window, text="My NFT calculator", font='bold')
title.grid(column=0, row=0, columnspan=3)

numOfLayersLbl = Label(window, text="Enter number of layers:")
numOfLayersLbl.grid(column=0, row=1)

numOfLayersNum = IntVar(window)
numOfLayersNum.set(5)

numOfLayersOption = OptionMenu(window, numOfLayersNum, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numOfLayersOption.grid(column=1, row=1)

#numOfLayersLbl = Label(window, text="Enter number of layers:")
#numOfLayersLbl.grid(column=0, row=1)
#
#numOfLayersTxt = Entry(window, width=40)
#numOfLayersTxt.insert(0, "127.0.0.1")
#numOfLayersTxt.grid(column=1, row=1, columnspan=2)
def refreshLayers():
    try:
        for i in range(10):
            name = str(i)+"label"
            name.destroy()
    except:
        pass

    for i in range(numOfLayersNum.get()):
        name = str(i)+"label"
        name = Label(window, text="Enter username:")
        name.grid(column=0, row=i+2)

#btn = Button(window, text="apply", command=refreshLayers)
#btn.grid(column=2, row=1)


allLayersMaxLbl = Label(window, text="Enter number of traits for each layer:")
allLayersMaxLbl.grid(column=0, row=2)

allLayersMaxTxt = Entry(window, width=40)
allLayersMaxTxt.insert(0, "3 6 5 4 3")
allLayersMaxTxt.grid(column=1, row=2, columnspan=2)

combinationsLengthLbl = Label(window, text="Enter number of traits that cannot repeat:")
combinationsLengthLbl.grid(column=0, row=3)

combinationsLengthTxt = Entry(window, width=40)
combinationsLengthTxt.insert(0, "4")
combinationsLengthTxt.grid(column=1, row=3, columnspan=2)



def runCalculator():
    global numOfLayers, allLayersMax, combinationsLength

    numOfLayers = int(numOfLayersNum.get())

    tempMyList  = allLayersMaxTxt.get().split()
    allLayersMax = []
    for num in tempMyList:
        allLayersMax.append(int(num))
    #allLayersMax = [2, 2, 2, 2]
    #print(allLayersMax)
    #exit()
    # Pocet attributu co se nesmi opakovat
    combinationsLength = int(combinationsLengthTxt.get())

    calculateIt(combinationsLength, numOfLayers, allLayersMax)

btn = Button(window, text="Run calculator!", command=runCalculator)
btn.grid(column=1, row=4)

window.mainloop()
