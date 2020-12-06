with open('input.txt') as fp:
    lines = fp.readlines()

def countHits(columnMove, rowMove):
    value = 0
    pos = 0
    for i, element in enumerate(lines):
        if i % rowMove == 0 or rowMove == 1:
            if element[pos] == '#':
                value += 1
            pos += columnMove
            if pos > 30:
                pos -= 31
                
print("Answer 1: " + str(countHits(3,1)))
print("Answer 2: " + str(countHits(3,1) * countHits(1,1) * countHits(5,1) * countHits(1,2) * countHits(7,1)))