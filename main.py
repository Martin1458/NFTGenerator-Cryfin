from PIL import Image 
from IPython.display import display 
import random
import json
import os
import shutil
from partsManager import *
from jsonToCsv import *
#Path k castem
pathToParts = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator2\Parts"

outputFolder = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator2\Output"

totalImages = 1000
allImages = []

def createNewImage():
    
    newImage = {}
    row = []

    backgroundChoice = random.choices(backgroundNames, backgroundWeights)[0]
    newImage ["Background"] = backgroundChoice
    bodyChoice = random.choices(bodyNames, bodyWeights)[0]
    newImage ["Body"] = bodyChoice
    highlightChoice = random.choices(highlightNames, highlightWeights)[0]
    newImage ["Highlight"] = highlightChoice
    outlineChoice = random.choices(outlineNames, outlineWeights)[0]
    newImage ["Outline"] = outlineChoice
    lightChoice = random.choices(lightNames, lightWeights)[0]
    newImage ["Light"] = lightChoice
    
    if newImage in allImages:
        return createNewImage()
    else:
        return newImage
    
    
for i in range(totalImages): 
    
    newTraitImage = createNewImage()
    
    allImages.append(newTraitImage)

#True pokud nejsou duplikaty
def allImagesUnique(allImages):
    seen = list()
    return not any(i in seen or seen.append(i) for i in allImages)


print("Are all images unique?", allImagesUnique(allImages))



#Prida ID ke kazdemu obrazku
i = 0
for item in allImages:
    item["tokenId"] = i
    i = i + 1

#Zapsat vygenerovane nft do database
NFTNewDatabase(allImages, r'C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator2\NFTData.csv')

#print(allImages)

#Kolik je jakych casti
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
    
print("Background count:"+str(backgroundCount))
print("Body count:"+str(bodyCount))
print("Highlight count:"+str(highlightCount))
print("Outline count:"+str(outlineCount))
print("Light count:"+str(lightCount))


if not os.path.isdir(outputFolder):
    os.mkdir(outputFolder)

outDirFiles = os.listdir(outputFolder)
decisionOutFolder = False
while(not decisionOutFolder):
    if len(outDirFiles) != 0:
        notEmptyDir = input("Warning! Output directory is not empty. Delete contents of output folder? [Y/N]")
        if notEmptyDir == "Y" or notEmptyDir == "y":
            decisionOutFolder = True
            shutil.rmtree(outputFolder)
            print("Output folder was deleted")
        elif notEmptyDir == "N" or notEmptyDir == "n":
            decisionOutFolder = True
            print("Output folder was not deleted")
        else:
            print("Invalid option")
    else:
        decisionOutFolder = True

if not os.path.isdir(outputFolder):
    os.mkdir(outputFolder)

for item in allImages:

    im1 = Image.open(os.path.join(pathToParts, backgroundFiles[item["Background"]])).convert('RGBA')
    im2 = Image.open(os.path.join(pathToParts, bodyFiles[item["Body"]])).convert('RGBA')
    im3 = Image.open(os.path.join(pathToParts, highlightFiles[item["Highlight"]])).convert('RGBA')
    im4 = Image.open(os.path.join(pathToParts, outlineFiles[item["Outline"]])).convert('RGBA')
    im5 = Image.open(os.path.join(pathToParts, lightFiles[item["Light"]])).convert('RGBA')

    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)

                     

    #Convert to RGB
    rgbIm = com4.convert('RGB')
    fileName = str(item["tokenId"]) + ".png"
    rgbIm.save(os.path.join(outputFolder, fileName))
    print("Image {} created with parameters: {}".format(fileName, item))