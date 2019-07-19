import csv

stateDict = {}
symbols = []
with open('state_chart.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            firstColumn = True
            for ele in row:
                if firstColumn:
                    firstColumn = False
                    pass
                print("appending element = "+ele)
                symbols.append(ele)
            line_count += 1
        else:
            i = 0
            firstState = True
            for nextState in row:
                if not row[0] in stateDict:
                    stateDict[row[0]] = {}
                if firstState:
                    firstState = False
                    pass
                print("row[0] == " + row[0])
                print("symbole[] length == " + str(len(symbols)) + " i == " + str(i))
                print("symbols[i] == " + symbols[i])
                print("nextState == " + nextState)
                stateDict[row[0]][symbols[i]] = (nextState,None)
                i += 1
        line_count += 1

print(stateDict)
