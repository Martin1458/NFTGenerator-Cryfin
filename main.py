import collections
import itertools
import json
import os
import random
import shutil
from itertools import combinations

from IPython.display import display
from PIL import Image

from partsManager import *

# Path k castem
pathToParts = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator11\Parts"

# Path do slozky kam se vyrenderuji obrazky
outputFolder = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator11\Output"

# Path k json souboru
outputJson = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator11\NFTs.json"

outputJsonFolder = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator11\Jsons\\"

outputResizeFolder = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator11\OutputResize"

# Pocet obrazku k vytvoreni
#totalImages = int(input("How many images should I create? "))
#totalImages = 20
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
# Pocet attributu co se smi opakovat
cobinationsLength = 3
# Read variable name (must be a tuple)
imgSize = (350, 350)

skipDecisions = True

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

cobinationsLength += 1
# Tato funkce vrati pocet kazdeho elementu, kolikrat se opakuje v myList
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
        #print('{} is {} times in all images'.format(item, myList.count(item)))

    fullList = nullParts

    for item in tempAllDuplicates:
        fullList[item] = tempAllDuplicates[item]


    #print(tempAllDuplicates)
    return fullList


# Test findDuplicates (pokud funguje napise "john")
# myList = ["john", "marry", "john", "james"]
# myBool, myDuplicate = findDuplicates(myList)
# print(myDuplicate)
def getDestination(xxxx):

    lastDest = ''
    someInt = -1
    if "\\" in xxxx:
        while lastDest=='':
            lastDest = xxxx.split('\\')[someInt]
            someInt -= 1
    elif "/" in xxxx:
        while lastDest=='':
            lastDest = xxxx.split('/')[someInt]
            someInt -= 1
    else:
        print("Path {} invalid".format(xxxx))
        exit()

    # print("-{}-".format(xxxx))
    # print("-{}-".format(lastDest))
    # print("-{}-".format(xxxx.split('\\')[-2]))
    # print("-{}-".format(xxxx.split('\\')[-1]))
    return lastDest


def checkFolder(xxx):
    if skipDecisions == False:

        if not os.path.isdir(xxx):
            os.mkdir(xxx)

        outDirFiles = os.listdir(xxx)
        decisionOutFolder = False
        while(not decisionOutFolder):
            if len(outDirFiles) != 0:
                notEmptyDir = input("Warning! {} directory is not empty. Delete contents of {} folder? [Y/N]: ".format(getDestination(xxx), getDestination(xxx)))
                if notEmptyDir.lower() == 'y':
                    decisionOutFolder = True
                    shutil.rmtree(xxx)
                    print("{} folder was deleted\n".format(getDestination(xxx)))
                elif notEmptyDir.lower() == 'n':
                    decisionOutFolder = True
                    print("{} folder was not deleted\n".format(getDestination(xxx)))
                else:
                    print("Invalid option")
            else:
                decisionOutFolder = True

        if not os.path.isdir(xxx):
            os.mkdir(xxx)

# Tato funkce vygeneruje originalni obrazek
def createNewImage(chosenTraits):
    # global = promenne ktere ma tato funkce pravo menit
    global allImages, allAttributeCombinations, newAttributes, newAttributesCollection, tempAllAttributeCombinations, allParts, tempAllParts

    # print("Img num:     "+str(len(allImages)))
    # vytvor/vynuluj list pro vytvoreni noveho ojbrazku
    newImage = {}

    # vyber "Background", "Body", "Highlight", "Outline" a "Light" podle tabulek z partsManager.py
    newImage ["Background"] = backgroundNames[chosenTraits[0]-1]
    newImage ["Body"] = bodyNames[chosenTraits[1]-1]
    newImage ["Highlight"] = highlightNames[chosenTraits[2]-1]
    newImage ["Outline"] = outlineNames[chosenTraits[3]-1]
    newImage ["Light"] = lightNames[chosenTraits[4]-1]

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
    for item in combinations(thisAttributes, cobinationsLength):
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
    allPartsCount = findElementXTimes(tempAllParts)

    # Zkontroluje pro kazdou trait zda se jiz nevyskytuje vicekrat nez by mela
    for item in maxParts:
        if maxParts[item] != 0:
            if allPartsCount[item] > maxParts[item]:
                thisDuplicate = True

    # ukaze duplikat pokud existuje, jinak napise None
    #print(thisDuplicateItem)

    # pokud se jiz duplikat nasel, funkce createNewImage se restartuje
    if thisDuplicate:
        # prida 1 k poctu pokusu k vytvoreni tohoto obrazku
        return 'duplicate'

    # Ted kdyz uz  jsme se zbavili duplikatu, zapiseme aktualni kombinace do allAttributeCombinations
    # (Aby jsme mohli zkontrolovat dalsi obrazky)
    for item in combinations(thisAttributes, cobinationsLength):
        allAttributeCombinations.append(item)

    # Zapise nove
    for item in newImage:
        allParts.append(newImage[item])

    # Zkontroluje zda obrazek jiz neexistuje
    if newImage in allImages:
        print(newImage)
        print("A whole image is repeating. How? IDK")
        return 'duplicate'
    else:
        print("Img num: "+str(len(allImages))+"; chosenTraits: "+str(chosenTraits))
        # Ted uz by nemeli existovat zadne duplikaty, vratime tedy vybrane attributy
        return newImage

# Tato funkce pomoci createNewImage vytvori danny pocet obrzku a projistotu je znovu zkontroluje pro duplikaty
def createAllImages():
    global allImages, allAttributeCombinations, newAttributes, newAttributesCollection

    #chosenTraits = [0, 0, 0, 0, 0]
    #allLayersMax = [3, 6, 5, 4, 3]
    allLayersMax = [len(backgroundNames), len(bodyNames), len(highlightNames), len(outlineNames), len(lightNames)]
    ranges = [range(1, n+1) for n in allLayersMax]

    someList = []
    for v in itertools.product(*ranges):
        someList.append(list(v))

    print(str(len(someList)))


    for chosenTraits in someList:
        # print("chosenTraits: "+str(chosenTraits))
        newTraitImage = createNewImage(chosenTraits)
        #newTraitImage = 'duplicate'
        # pokud createNewImage nevrati error, zapise obrazek do allImages, jinak ukonci script.
        if newTraitImage != 'error' and newTraitImage != 'duplicate':
            allImages.append(newTraitImage)
        elif newTraitImage == 'duplicate':
            pass

        if newTraitImage == 'error':
            print("An error has occured")
            exit()


    # Tato funkce zkontroluje allImages pro duplikaty
    def allImagesUnique(listToCheck):
        # 'mezivypocetny' list seen
        seen = list()
        return not any(i in seen or seen.append(i) for i in listToCheck)

    # True pokud nejsou duplikaty
    print("Are all images unique?", allImagesUnique(allImages))

# Volani hlavni funkce pro vytvoreni obrazku
createAllImages()
#print("allAttributeCombinations: "+str(allAttributeCombinations))
newAllAttributeCombinations = []
for i in allAttributeCombinations:
    newline = []
    for e in i:
        newline.append(allFiles[e])
    newAllAttributeCombinations.append(newline)
#print("newAllAttributeCombinations: "+str(newAllAttributeCombinations))
# convert to 2d array pro checking
# allAttributes = []
# for nft in allImages:
#     allAttributes.append([])
#     for attribute in nft:
#         allAttributes[allImages.index(nft)].append(nft[attribute])
# print(allAttributes)

# Prida ID ke kazdemu obrazku
i = 0
for item in allImages:
    item['tokenId'] = i
    i = i + 1

# Generovani json souboru

if skipDecisions == False:
    jsonItTxt = input("Should I create jsons? [Y/N]: ")
    jsonIt = [False, True][jsonItTxt.lower() == 'y']
else:
    jsonIt = True

if jsonIt:

    checkFolder(outputJsonFolder)

    allJsonImagesList = []
    for image in allImages:
        attributes = []
        for item in image:
            if item != 'tokenId':
                attribute = {
                    "trait_type": item,
                    "value": image[item]
                }
                attributes.append(attribute)

        oneImage = {
            "name": "#{}".format(image['tokenId']),
            "description": "This is Lo-Fish num: {}".format(image['tokenId']),
            "image": "https://bitterfly.io/home/wp-content/uploads/2022/09/"+str(image['tokenId'])+".png",
            "edition": image['tokenId']+1,
            "index": image['tokenId'],
            "attributes": attributes
            }
        #print(oneImage)
        allJsonImagesList.append(oneImage)

        oneImageDump = json.dumps(oneImage, indent=4, sort_keys=False)

        with open(outputJsonFolder+str(allImages.index(image))+".json", "w") as outfile:
        # zapise allJsonImages do outputJson
            outfile.write(oneImageDump)

    # konvertuje allJsonImagesList do json formatu a ulozi do allJsonImages
    allJsonImages = json.dumps(allJsonImagesList, indent=4, sort_keys=False)

    # vytvori/vymaze content outputJson
    open(outputJson, "w").close()

    # otevre outputJson
    with open(outputJson, "w") as outfile:
        # zapise allJsonImages do outputJson
        outfile.write(allJsonImages)

# Kolik je jakych casti
backgroundCount = {}
for item in backgroundNames:
    backgroundCount[item] = 0

bodyCount = {}
for item in bodyNames:
    bodyCount[item] = 0

highlightCount = {}
for item in highlightNames:
    highlightCount[item] = 0

outlineCount = {}
for item in outlineNames:
    outlineCount[item] = 0

lightCount = {}
for item in lightNames:
    lightCount[item] = 0

for image in allImages:
    backgroundCount[image["Background"]] += 1
    bodyCount[image["Body"]] += 1
    highlightCount[image["Highlight"]] += 1
    outlineCount[image["Outline"]] += 1
    lightCount[image["Light"]] += 1

# Napise pocet vyskytu kazde casti
print("Background count :"+str(backgroundCount))
print("Body count       :"+str(bodyCount))
print("Highlight count  :"+str(highlightCount))
print("Outline count    :"+str(outlineCount))
print("Light count      :"+str(lightCount)+"\n")
print("Num of images    :"+str(len(allImages)))
#
#print(allParts)
#print(len(allParts))

if skipDecisions == False:
    # Script se zepta pokud ma vypocitane obrazky vyrenderovat
    renderEmTxt = input("Should I render those Images? [Y/N]: ")
    renderEm = [False, True][renderEmTxt.lower() == 'y']
else:
    renderEm = True

# Pokud ma script obrazky vyrendrovat, ucini tak
if renderEm:

    checkFolder(outputFolder)

    checkFolder(outputResizeFolder)

    # vyrenderuje vsechny obrazky
    for item in allImages:

        # vygeneruje kazdou vrstvu oddelene
        im1 = Image.open(os.path.join(pathToParts, backgroundFiles[item["Background"]])).convert('RGBA')
        im2 = Image.open(os.path.join(pathToParts, bodyFiles[item["Body"]])).convert('RGBA')
        im3 = Image.open(os.path.join(pathToParts, highlightFiles[item["Highlight"]])).convert('RGBA')
        im4 = Image.open(os.path.join(pathToParts, outlineFiles[item["Outline"]])).convert('RGBA')
        im5 = Image.open(os.path.join(pathToParts, lightFiles[item["Light"]])).convert('RGBA')

        # Spoji vsechny vygenerovane vrstvy
        com1 = Image.alpha_composite(im1, im2)
        com2 = Image.alpha_composite(com1, im3)
        com3 = Image.alpha_composite(com2, im4)
        com4 = Image.alpha_composite(com3, im5)

        rgbIm = com4.convert('RGB')

        # Pojmenuje obrazek tokenID.png
        fileName = str(item["tokenId"]) + ".png"

        # Ulozi obrazek do outputFolder
        rgbIm.save(os.path.join(outputFolder, fileName))

        ss = com4.resize(imgSize)
        rgbIm = ss.convert('RGB')

        rgbIm.save(os.path.join(outputResizeFolder, fileName))

        print("Image {} created with parameters: {}".format(fileName, item))
        # exit()
