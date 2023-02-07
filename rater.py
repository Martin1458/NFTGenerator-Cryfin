import json
import csv
from collections import Counter
from partsManager import *

# Input
createdCsv = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator17\created.csv"
# Output
attributeRatingJson = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator17\output.json"
NFTsJson = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator17\NFTs.json"
csvRating = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator17\rating.csv"
sortedCreatedCsv = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator17\sortedCreated.csv"

def createOneImage(xx):
    newImage = []

    newImage.append(backgroundNames[int(xx[0])-1])
    newImage.append(bodyNames[int(xx[1])-1])
    newImage.append(highlightNames[int(xx[2])-1])
    newImage.append(outlineNames[int(xx[3])-1])
    newImage.append(lightNames[int(xx[4])-1])

    return newImage

with open(createdCsv) as file:
    reader = csv.reader(file)
    createdCsvData = []
    for row in reader:
        createdCsvData.append(row)


newCreatedCsvData = [list( map(int,i) ) for i in createdCsvData]
zipedCreatedCsvData = list(zip(*newCreatedCsvData))
#print(zipedCreatedCsvData)
allLayerNames = [backgroundNames, bodyNames, highlightNames, outlineNames, lightNames]

if len(zipedCreatedCsvData) == len(allLayerNames):
    print("All good")
else:
    print("wrong layer count")

attributeRatingJsonData = {}
for i in range(len(allLayerNames)):
    count = Counter(zipedCreatedCsvData[i])
    #print(count)
    for e in range(len(count)):
        #print("i: "+str(i)+"; e: "+str(e))
        #print(allLayerNames[i][e])
        #print(list(count.items())[e][1])
        attributeRatingJsonData[allLayerNames[i][e]] = list(count.items())[e][1]


print("createdCsvData: "+str(createdCsvData))
print("Verifying json file...")

totalNumCount = 0
for i in attributeRatingJsonData:
    totalNumCount += attributeRatingJsonData[i]

if float(totalNumCount)/float(len(createdCsvData)) == len(createdCsvData[0]):
    print("All good")
else:
    print("Some numbers dont add up.")
    if input("Continue? [Y/N]: ").lower() == "y":
        pass
    else:
        print("Exitting...")
        exit()


for i in attributeRatingJsonData:
    attributeRatingJsonData[i] = attributeRatingJsonData[i]/len(createdCsvData)

# Pocet kazde jednotlive attributy: DarkBG, MidBG...  / celkovy pocet obrazku.
print("attributeRatingJsonData: "+str(attributeRatingJsonData))

formatAttributeRatingJsonData = json.dumps(attributeRatingJsonData, indent=4, sort_keys=False)

open(attributeRatingJson, "w").close()
with open(attributeRatingJson, "w") as outfile:
    outfile.write(formatAttributeRatingJsonData)


allImages = []
allTraits = []
with open(createdCsv) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        allTraits.append(row)

for traits in allTraits:
    allImages.append(createOneImage(traits))

print("allImages"+str(allImages))

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

csvHeader = ["id", "allImagesRatingData", "allImagesRatingPercentage", "allImagesRatingPercentageZeroToHundred"]

open(csvRating, "w").close()
with open(csvRating, "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(csvHeader)
    for w in range(len(allImagesRatingData)):
        writer.writerow([w, allImagesRatingData[w], allImagesRatingPercentage[w], allImagesRatingPercentageZeroToHundred[w], createdCsvData[w], ])
    #writer.writerows(allImagesRatingPercentage)
    #writer.writerows(allImagesRatingPercentageZeroToHundred)

sortedCreatedCsvDataAscending  = [x for _, x in sorted(zip(allImagesRatingData, createdCsvData))]
sortedCreatedCsvDataDescending = sortedCreatedCsvDataAscending
sortedCreatedCsvDataDescending.reverse()


open(sortedCreatedCsv, "w").close()
with open(sortedCreatedCsv, "w", newline='') as outfile:
    writer = csv.writer(outfile)
    for w in range(len(sortedCreatedCsvDataDescending)):
        writer.writerow(sortedCreatedCsvDataDescending[w])
