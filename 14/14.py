import time
start = time.time()
with open('c:\\repos\\AoC2020\\14\\input.txt') as fp:
    lines = [line.rstrip().replace("mem[", "").replace("]", "").split(" = ") for line in fp]

mem = dict()
for i, line in enumerate(lines):
    if line[0] == "mask":
        mask = line[1]
    else:
        temp = format(int(line[1]), 'b').rjust(36, "0")
        value = 0
        for i in range(0, 36):
            if mask[i] != "X":
                value += int(mask[i]) << (35 - i)
            else:
                value += int(temp[i]) << (35 - i)
        mem[line[0]]  = value
print("Answer 1: " + str(sum(mem.values())))

mem = dict()
for i, line in enumerate(lines):    
    addresses = []
    if line[0] == "mask":
        mask = line[1]
    else:
        value = line[1]
        temp = format(int(line[0]), 'b').rjust(36, "0")
        for i in range(0, 36):
            if mask[i] == "X":
                if not addresses:
                    addresses.append("1")
                    addresses.append("0")
                else:
                    for j in range(len(addresses)):
                        tempAdd = addresses[j]
                        addresses[j] += "1"
                        addresses.append(tempAdd + "0")
            elif mask[i] == "1":
                if not addresses:
                    addresses.append("1")
                else:
                    for j in range(len(addresses)):
                        addresses[j] += "1"
            else:
                if not addresses:
                    addresses.append(temp[i])
                else:
                    for j in range(len(addresses)):
                        addresses[j] += temp[i]
        for address in addresses:
            mem[int(address, 2)] = int(value)
stop = time.time()
print("Answer 2: " + str(sum(mem.values())))
print(f"time {stop-start}")