import time
start = time.time()
with open('c:\\repos\\AoC2020\\15\\input.txt') as fp:
    lines = fp.readlines()

def list_rindex(li, x):
    for i in reversed(range(len(li))):
        if li[i] == x:
            return i
    return -1

numbers = lines[0].split(",")
while(len(numbers) < 2020):
    lastPos = list_rindex(numbers[:-1], numbers[-1])
    if(lastPos == -1):
        numbers.append("0")
    else:
        numbers.append(str(len(numbers) - 1 - lastPos))
stop = time.time()
print("Answer 1: " + numbers[-1])
print(f"time {stop-start}")

start = time.time()
numbers = lines[0].split(",")
prevNumbers = {}
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
    prevNumber = int(numbers[i])
    prevNumbers[prevNumber] = i
for i in range(len(numbers), 30000000):
    if numbers[-1] in prevNumbers:
        temp = i - 1 - prevNumbers[numbers[-1]]
    else:
        temp = 0
    prevNumbers[numbers[-1]] = len(numbers) - 1
    numbers.append(temp)
stop = time.time()
print("Answer 2: " + str(numbers[-1]))
print(f"time {stop-start}")
