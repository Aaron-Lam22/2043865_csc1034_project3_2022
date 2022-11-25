import csv
import datetime

filename = 'clients.csv'


def ViewClients():
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for lines in reader:
            print(lines)


def addClient(title, last_name, first_name, pronouns, email, date_of_birth, occupation, balance, overdraft):
    if not checkClient(date_of_birth, balance, overdraft):
        print("Client input declined")
        return

    clientID = 0
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for line in enumerate(reader):
            clientID = int(line[0]) + 1

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(
            [clientID, title, last_name, first_name, pronouns, email, date_of_birth, occupation, balance, overdraft])


def checkClient(date_of_birth, balance, overdraft):
    try:
        isinstance(float(balance), float)
    except:
        print("Balance is not decimal")
        return False
    try:
        isinstance(float(overdraft), float)
    except:
        print("Overdraft is not decimal")
        return False

    if not checkDOB(date_of_birth):
        return False

    return True


def appendCSV(string):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows([string])


def catagoriesCSV():
    fields = (
    'ClientID', 'title', 'last_name', 'first_name', 'pronouns', 'email', 'date_of_birth', 'occupation', 'balance',
    'overdraft')
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(fields)


def checkDOB(date_of_birth):
    try:

        datetimeArray = date_of_birth.split(' ')[0].split('-')

        validDateTime = True
        if int(datetimeArray[0]) > 2100 or int(datetimeArray[0]) < 1900:
            validDateTime = False
        if int(datetimeArray[1]) > 12 or int(datetimeArray[1]) < 1:
            validDateTime = False
        if int(datetimeArray[2]) > 31 or int(datetimeArray[2]) < 1:
            validDateTime = False
        if not validDateTime:
            print(
                "Date of Birth is not given correctly, please input Date of birth correctly in the format of YYYY-MM-DD, otherwise Date of Birth is inputted incorrectly")
            return False
    except:
        print(
            "Date of Birth is not given correctly, please input Date of birth correctly in the format of YYYY-MM-DD, otherwise Date of Birth is inputted incorrectly")
        return False
    return True


def checkID(clientID):
    if clientID < 0:
        print("Input error, value cannot fall below 0, unlike my standards of you")
        return False
    try:
        if not isinstance(int(clientID), int):
            print("Input Error: client ID is not an integer")
            return False
    except:
        print("Input Error: client ID is not an integer")
    return True


def editClient(clientNo, columnNo, newText):
    if not checkID(clientNo):
        return
    if columnNo == 6:
        if not checkDOB(newText):
            return
    if columnNo == 8 or columnNo == 9:
        try:
            isinstance(float(newText), float)
        except:
            print("Balance and Overdraft are not given as decimal values")
            return
    with open(filename, 'r') as file:
        linesList = []
        lines = file.readlines()
        count = 0
        for line in lines:
            if count > 0:
                if int(line[0]) == clientNo:
                    lineArray = line.split(',')
                    lineArray[columnNo] = newText
                    text = ""

                    for g in lineArray:
                        text = text + "," + g
                    line = str(text[1:])
            linesList.append(line)
            count += 1
    with open(filename, 'w', newline='') as file:
        file.writelines(linesList)


def getClientValue(clientNo, columnNo):
    if not checkID(clientNo):
        return
    with open(filename, 'r') as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            if count > 0:
                if int(line[0]) == clientNo:
                    lineArray = line.split(',')
                    return lineArray[columnNo]
                count += 1


def deleteClient(clientNo):
    if not checkID(clientNo):
        return

    with open(filename, 'r') as file:
        lineList = []
        lines = file.readlines()
        count = 0
        for line in lines:
            if count == 0:
                lineList.append(line)
            if count > 0:
                if int(line[0]) != clientNo:
                    if int(line[0]) > clientNo:
                        lineArray = line.split(',')
                        lineArray[0] = str(int(line[0]) - 1)
                        text = ""
                        for g in lineArray:
                            text = text + "," + g
                        line = str(text[1:])
                    lineList.append(line)
            count += 1
    with open(filename, 'w', newline='') as file:
        file.writelines(lineList)


def changeMoney(clientNo, change):
    if not checkID(clientNo):
        return

    currentMoney = getClientValue(clientNo, 8)
    newMoney = float(currentMoney) + float(change)
    if checkOverdraft(clientNo, newMoney):
        newMoney = newMoney - 5
    editClient(clientNo, 7, str(newMoney))


def checkOverdraft(clientNo, newMoney):
    currentoverdraft = float(getClientValue(clientNo, 8))
    if newMoney < -abs(currentoverdraft):
        return True


def searchByDOB(inputDOB):
    if not checkDOB(inputDOB):
        return

    datetimeArray = inputDOB.split('-')
    DOB = datetime.datetime(int(datetimeArray[0]), int(datetimeArray[1]), int(datetimeArray[2]))
    viewConditional(6, str(DOB))


def viewConditional(columnNo, searchTerm):
    with open(filename, 'r') as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            if count == 0:
                print(line)
            if count > 0:
                lineArray = line.split(',')
                if columnNo == 6:
                    if str(lineArray[columnNo]).__contains__(searchTerm):
                        print(line)
                    else:
                        if str(lineArray[columnNo]).lower() == searchTerm.lower():
                            print(line)

                count += 1


def viewIndebtedClients():
    with open(filename, 'r') as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            if count == 0:
                print(line)
            if count > 0:
                lineArray = line.split(',')
                if float(lineArray[7]) < 0:
                    print(line)
            count += 1

