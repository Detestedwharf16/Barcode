import csv

names = []
timeIn = []
timeOut = []
ui = input("Who are you looking for?")
testdex = []

with open('untitled.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        names.append(row[1])
        timeIn.append(row[2])
        timeOut.append(row[3])




for index, value in enumerate(names):
    # If the current value matches something, append the index to the list
    if value == ui:
        testdex.append(index)


search = timeIn[len(testdex)]
search2 = timeOut[len(testdex)]




print(testdex)
print(ui,"entered at", search, "and left at", search2)
