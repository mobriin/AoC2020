with open('input.txt') as fp:
    lines = fp.readlines()
    
okPw = 0
for x in lines:
    y = x.splitlines()
    one = x.split("-")
    min = int(one[0])

    two = one[1].split(" ")
    max = int(two[0])
    letter = two[1].split(":")[0]

    pw =two[2]
    charCount = 0
    for c in pw:
      if c == letter:
        charCount += 1
    if charCount >= min and charCount <= max:
        okPw +=1
print("Answer 1: " + str(okPw))

okPw = 0
for x in lines:
    y = x.splitlines()
    one = x.split("-")
    firstPos = int(one[0]) - 1

    two = one[1].split(" ")
    secondPos = int(two[0]) - 1
    letter = two[1].split(":")[0]

    pw =two[2]
    if pw[firstPos] == letter and pw[secondPos] != letter:
        okPw += 1
    elif pw[firstPos] != letter and pw[secondPos] == letter:
        okPw += 1
print("Answer 2: " + str(okPw))