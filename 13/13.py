
import math
with open('c:\\repos\\AoC2020\\13\\input.txt') as fp:
    lines = [line.rstrip() for line in fp]

time = int(lines[0])
busses = lines[1].split(",")

selBus = math.inf
for bus in busses:
    if bus.isdigit():
        if int(bus) - (time % int(bus)) < selBus - (time % selBus):
            selBus = int(bus)
print("Answer 1: " + str(selBus * (selBus - (time % selBus))))

busList = []
for i, bus in enumerate(busses):
    if bus != "x":
        busList.append((i, int(bus)))

time = 0
inc = busList[0][1]
for i, bus in busList[1:]:
        while (time + i) % bus != 0:
            time += inc
        inc *= bus
print("Answer 2: " + str(time))
    
