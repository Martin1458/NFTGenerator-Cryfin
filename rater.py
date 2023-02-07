import json
import csv
from partsManager import *

countJson = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator12\count.json"
NFTsJson = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator12\NFTs.json"
createdCsv = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator12\created.csv"
attributeRatingJson = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator12\output.json"
ratingJson = r"C:\Users\marti\Desktop\PythonProjects\AxieInfinity\NFTImgGenerator12\rating.json"

def createOneImage(xxx):
    newImage = {}

    newImage ["Background"] = backgroundNames[int(xxx[0])-1]
    newImage ["Body"] = bodyNames[int(xxx[1])-1]
    newImage ["Highlight"] = highlightNames[int(xxx[2])-1]
    newImage ["Outline"] = outlineNames[int(xxx[3])-1]
    newImage ["Light"] = lightNames[int(xxx[4])-1]

    return newImage


f = open(countJson)
attributeRatingJsonData = json.load(f)
f.close()


print("Verifying json file...")

y = 0
for i in attributeRatingJsonData:
    x = 0
    for item in attributeRatingJsonData[i]:
        x += attributeRatingJsonData[i][item]
        #print(attributeRatingJsonData[i][item])
    y += x

print(attributeRatingJsonData)

if float(y)/float(x) == len(attributeRatingJsonData):
    print("All good")
else:
    print("Ay yo, who fucked up?")
    if input("Continue? [Y/N]: ").lower() == "y":
        pass
    else:
        print("Exitting...")
        exit()


for i in attributeRatingJsonData:
    for item in attributeRatingJsonData[i]:
        attributeRatingJsonData[i][item] = attributeRatingJsonData[i][item]/x

print(attributeRatingJsonData)


for i in attributeRatingJsonData:
    xx = 0
    for item in attributeRatingJsonData[i]:
        xx  += attributeRatingJsonData[i][item]
    print(xx)
attributeRatingJsonData = json.dumps(attributeRatingJsonData, indent=4, sort_keys=False)

print(attributeRatingJsonData)


open(attributeRatingJson, "w").close()

with open(attributeRatingJson, "w") as outfile:
    outfile.write(attributeRatingJsonData)

allImages = []
allTraits = []
with open(createdCsv) as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader: # each row is a list
        allTraits.append(row)

for traits in allTraits:
    allImages.append(createOneImage(traits))

#i = 0
#for item in allImages:
#    item['tokenId'] = i
#    i = i + 1

print(allImages)
exit()
allImagesRatings = []
for image in allImages:
    xxxx = 0
    for attribute in image:
        xxxx += attributeRatingJsonData
    allImagesRatings.append(xxxx)

exit()

f = open(NFTsJson)
NFTsJsonData = json.load(f)
f.close()

ratingJsonData = {}
names = []
for i in NFTsJsonData:
    names.append({"name":i["name"]})


print(names)
