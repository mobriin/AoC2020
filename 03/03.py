with open('input.txt') as fp:
    lines = fp.readlines()

def countHits(columnMove, rowMove):
    value = 0
    pos = 0
    row = rowMove
    for i in lines:
        if row > 1:
            if row % rowMove == 0:
                if i[pos] == '#':
                    value += 1
                pos += 1
                if pos > 30:
                    pos -= 31
            row += 1
        else:
            if i[pos] == '#':
                value += 1
            pos += columnMove
            if pos > 30:
                pos -= 31
    return value

print("Answer 1:" + str(countHits(3,1)))

print("Answer 2: " + str(countHits(3,1) * countHits(1,1) * countHits(5,1) * countHits(1,2) * countHits(7,1)))