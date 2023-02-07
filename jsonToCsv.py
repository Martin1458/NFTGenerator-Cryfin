import csv

def NFTNewDatabase(jsonDatabase, pathToDB):
    
    dataJson = jsonDatabase
    pathToCsv = pathToDB

    someArray = []
    someRow = []
    headers = []
    for i in dataJson:
        for e in i:
            someRow.append(i[e])
        someArray.append(someRow)
        someRow = []

    for i in dataJson[0]:
        headers.append(i)

    open(pathToCsv, 'w').close()

    with open(pathToCsv, 'w', newline='') as f:
                writer = csv.writer(f)

                writer.writerow(headers)
                writer.writerows(someArray)
