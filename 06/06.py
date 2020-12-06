with open('input.txt') as fp:
    lines = fp.readlines()

groupAnswers = []
groupCounts = []
answerString = ""
groupCount = 0
for i in lines:
    if i == "\n":
        groupAnswers.append(answerString)
        groupCounts.append(groupCount)
        answerString = ""
        groupCount = 0

    else:
        groupCount += 1
        if i[len(i)-1:] == "\n":
            answerString += i[0:-1]
        else:
            answerString += i
groupAnswers.append(answerString)
groupCounts.append(groupCount)

firstAns = []
for i in groupAnswers:
    firstAns.append("".join(dict.fromkeys(i)))

count = 0

for i in firstAns:
    count += len(i)
print("Answer 1: " + str(count))

for i in range(len(groupAnswers)):
    groupAnswers[i] = sorted(groupAnswers[i])

count = 0
for i, element in enumerate(groupAnswers):
    groupRes = 0
    charCount = 1
    for x in range(len(element)):
        if groupCounts[i] == 1:
            count += len(element)
            break
        if x == len(element) - 1:
            break
        if element[x] == element[x+1]:
            charCount += 1
        elif element[x] != element[x+1]:
            charCount = 1
        if charCount == groupCounts[i]:
            count += 1

print("Answer 2: " + str(count))