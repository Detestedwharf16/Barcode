import csv


names = []
timeIn = []
timeOut = []
ui = input("Who are you looking for?")
testdex = []
TimeOutput1 = []
TimeOutput2 = []

with open('Untitled.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        names.append(row[0])
        timeIn.append(row[1])
        timeOut.append(row[2])


def times(name):
    for i in range(len(timeIn)):
        if names[i] == name:
            print('In:', timeIn[i])
            TimeOutput1.append(timeIn[i])
            print('Out:', timeOut[i])
            TimeOutput2.append(timeOut[i])



times(ui)

with open('Output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='excel', delimiter = ' ')
    writer.writerow([ui])
    for i in range(len(TimeOutput1)):
        writer.writerow([TimeOutput1[i]])
        writer.writerow([TimeOutput2[i]])
    #writer.writerow([TimeOutput1])


