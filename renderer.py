import collections
import itertools
import json
import os
import random
import shutil
import csv
from itertools import combinations
import pandas as pd
from IPython.display import display
from PIL import Image
import numpy as np
from partsManager import *

# Input
pathToParts = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator13\Parts"
outputFolder = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator13\Output"
outputJson = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator13\NFTs.json"
outputJsonFolder = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator13\Jsons\\"
csvCreated = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator13\created.csv"
outputResizeFolder = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator13\OutputResize"
# Output
countJson = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator13\count.json"

allImages = []
allParts = []
allPartsCount = {}
tempAllParts = []
thisAttributes = []
thisAttributeCombinations = []
imgSize = (350, 350)
skipDecisions = False

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

def createOneImage(xx):
    newImage = {}

    newImage ["Background"] = backgroundNames[int(xx[0])-1]
    newImage ["Body"] = bodyNames[int(xx[1])-1]
    newImage ["Highlight"] = highlightNames[int(xx[2])-1]
    newImage ["Outline"] = outlineNames[int(xx[3])-1]
    newImage ["Light"] = lightNames[int(xx[4])-1]

    return newImage

# df = pd.read_csv(csvCreated)
# allTraits = df.values

# CSVData = open(csvCreated)
# allTraits = np.genfromtxt(CSVData, delimiter=",")

allTraits = []
with open(csvCreated) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        allTraits.append(row)

for traits in allTraits:
    allImages.append(createOneImage(traits))

i = 0
for item in allImages:
    item['tokenId'] = i
    i = i + 1


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

        allJsonImagesList.append(oneImage)

        oneImageDump = json.dumps(oneImage, indent=4, sort_keys=False)

        with open(outputJsonFolder+str(allImages.index(image))+".json", "w") as outfile:

            outfile.write(oneImageDump)


    allJsonImages = json.dumps(allJsonImagesList, indent=4, sort_keys=False)


    open(outputJson, "w").close()


    with open(outputJson, "w") as outfile:

        outfile.write(allJsonImages)

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


    print("Background count :"+str(backgroundCount))
    print("Body count       :"+str(bodyCount))
    print("Highlight count  :"+str(highlightCount))
    print("Outline count    :"+str(outlineCount))
    print("Light count      :"+str(lightCount)+"\n")
    print("Num of images    :"+str(len(allImages)))

    #countData = {
    #    "backgroundCount": backgroundCount,
    #    "bodyCount": bodyCount,
    #    "highlightCount": highlightCount,
    #    "outlineCount": outlineCount,
    #    "lightCount": lightCount
    #}

    countData = backgroundCount | bodyCount | highlightCount | outlineCount | lightCount


    countDataJson = json.dumps(countData, indent=4, sort_keys=False)


    open(countJson, "w").close()


    with open(countJson, "w") as outfile:

        outfile.write(countDataJson)


if skipDecisions == False:

    renderEmTxt = input("Should I render those Images? [Y/N]: ")
    renderEm = [False, True][renderEmTxt.lower() == 'y']
else:
    renderEm = True


if renderEm:

    checkFolder(outputFolder)

    checkFolder(outputResizeFolder)


    for item in allImages:


        im1 = Image.open(os.path.join(pathToParts, backgroundFiles[item["Background"]])).convert('RGBA')
        im2 = Image.open(os.path.join(pathToParts, bodyFiles[item["Body"]])).convert('RGBA')
        im3 = Image.open(os.path.join(pathToParts, highlightFiles[item["Highlight"]])).convert('RGBA')
        im4 = Image.open(os.path.join(pathToParts, outlineFiles[item["Outline"]])).convert('RGBA')
        im5 = Image.open(os.path.join(pathToParts, lightFiles[item["Light"]])).convert('RGBA')


        com1 = Image.alpha_composite(im1, im2)
        com2 = Image.alpha_composite(com1, im3)
        com3 = Image.alpha_composite(com2, im4)
        com4 = Image.alpha_composite(com3, im5)

        rgbIm = com4.convert('RGB')


        fileName = str(item["tokenId"]) + ".png"


        rgbIm.save(os.path.join(outputFolder, fileName))

        ss = com4.resize(imgSize)
        rgbIm = ss.convert('RGB')

        rgbIm.save(os.path.join(outputResizeFolder, fileName))

        print("Image {} created with parameters: {}".format(fileName, item))
