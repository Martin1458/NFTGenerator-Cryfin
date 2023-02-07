import json
import csv
from partsManager import *

# Input
countJson = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator13\count.json"
NFTsJson = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator13\NFTs.json"
attributeRatingJson = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator13\output.json"
# Output


f = open(countJson)
attributeRatingJsonData = json.load(f)
f.close()

f = open(NFTsJson)
NFTsJsonData = json.load(f)
f.close()

print("Verifying json file...")


totalNumCount = 0
for i in attributeRatingJsonData:
    totalNumCount += attributeRatingJsonData[i]

if float(totalNumCount)/float(len(NFTsJsonData)) == len(NFTsJsonData[0]["attributes"]):
    print("All good")
else:
    print("Some numbers dont add up.")
    if input("Continue? [Y/N]: ").lower() == "y":
        pass
    else:
        print("Exitting...")
        exit()


for i in attributeRatingJsonData:
    attributeRatingJsonData[i] = attributeRatingJsonData[i]/len(NFTsJsonData)

# Pocet kazde jednotlive attributy: DarkBG, MidBG...  / celkovy pocet obrazku.
print("attributeRatingJsonData: "+str(attributeRatingJsonData))

formatAttributeRatingJsonData = json.dumps(attributeRatingJsonData, indent=4, sort_keys=False)

open(attributeRatingJson, "w").close()
with open(attributeRatingJson, "w") as outfile:
    outfile.write(formatAttributeRatingJsonData)


allImages = []
for image in NFTsJsonData:
    oneImage = []
    for attribute in image["attributes"]:
        oneImage.append(attribute["value"])
    allImages.append(oneImage)

# List vsech attibut pro kazdy obrazek: ['DarkBG', 'PinkB', 'WhiteHL', 'RedOL', 'WhiteL'], ['DarkBG',...
print("allImages: "+str(allImages))

allImagesRatingData = []
for image in allImages:
    oneImage = float(0)
    for attribute in image:
        oneImage += float(attributeRatingJsonData[attribute])
    allImagesRatingData.append(oneImage)

# Pro kazdy obrazek z allImages, soucet zpravnych cisel z attributeRatingJsonData
print("allImagesRatingData: "+str(allImagesRatingData))

hundredPercent = allImagesRatingData[0]
for number in allImagesRatingData:
    if number > hundredPercent:
        hundredPercent = number

zeroPercent = allImagesRatingData[0]
for number in allImagesRatingData:
    if number < zeroPercent:
        zeroPercent = number


allImagesRatingPercentage = []
for i in allImagesRatingData:
    allImagesRatingPercentage.append((float(i)/float(hundredPercent)) * 100)

# Procenta z allImagesRatingData, max z allImagesRatingData = 100%; 0 = 0%
print("allImagesRatingPercentage: "+str(allImagesRatingPercentage))

allImagesRatingPercentageZeroToHundred = []
for i in allImagesRatingData:
    allImagesRatingPercentageZeroToHundred.append(((float(i) - float(zeroPercent)) * 100) / (float(hundredPercent) - float(zeroPercent)))

# Procenta z allImagesRatingData, max z allImagesRatingData = 100%; min z allImagesRatingData = 0%
print("allImagesRatingPercentageZeroToHundred: "+str(allImagesRatingPercentageZeroToHundred))
