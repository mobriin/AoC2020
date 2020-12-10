with open('input.txt') as fp:
    lines = fp.readlines()

numbers = []
for i in lines:
    numbers.append(int(i))

firstList = []
for i in numbers:
    if len(firstList) < 25:
        firstList.append(i)
        continue
    firstPos = 0
    sumFound = False
    while firstPos < len(firstList) - 1 and not sumFound:
        secondPos = firstPos + 1
        while secondPos < len(firstList) and not sumFound:
            if firstList[firstPos] + firstList[secondPos] == i:
                firstList.pop(0)
                firstList.append(i)
                sumFound = True
                break
            secondPos += 1
        firstPos += 1
    if not sumFound:
        print("Answer 1: " + str(i))
        answerOne = i
        break

while firstPos < len(numbers) - 1:
    secondNumbers = []
    secondNumbers.append(numbers[firstPos])
    secondPos = firstPos + 1
    while secondPos < len(numbers) and sum(secondNumbers) < answerOne:
        secondNumbers.append(numbers[secondPos])
        secondPos += 1
    if sum(secondNumbers) == answerOne:
        secondNumbers.sort()
        print("Answer 2: " + str(secondNumbers[0] + secondNumbers[-1]))
        break
    firstPos += 1