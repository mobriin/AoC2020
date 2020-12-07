with open('input.txt') as fp:
    lines = fp.readlines()

splitInput = []
for row in lines:
    temp = row.replace(" bags", " bag").replace(" bag", "").replace(".", "").replace("\n", "").replace(",", "")
    splitInput.append(temp.split(" contain "))  

dict = {}
for row in splitInput:
    temp = row[1].split(" ")
    tempList = []
    for i in range(int(len(temp)/3)):
        tempList.append((temp[1+i*3] + " " + temp[2+i*3], temp[i*3]))
    dict[row[0]] = tempList

def findBag(color):
    bagFound = False
    myTup = dict[color]
    for i in myTup:
        if i[0] == "shiny gold":
            bagFound = True
            break
        else:
            if(findBag(i[0])):
                bagFound = True
    return bagFound

bagCount = 0
for value in dict:
    if(findBag(value)):
        bagCount += 1
        print(value)
print("Answer 1: " + str(bagCount))

def countBags(color):
    bagCount = 0
    myTup = dict[color]
    for i in myTup:
        bagCount += int(i[1])
        for _ in range(int(i[1])):
            bagCount += countBags(i[0])
    return bagCount
print("Answer 2: " + str(countBags("shiny gold")))