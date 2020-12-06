import re
with open('input.txt') as fp:
    lines = fp.readlines()

passports = []
passString = ""
for i in lines:
    if i == "\n":
        passports.append(passString)
        passString = ""

    else:
        if i[len(i)-1:] == "\n":
            passString += i[0:-1] + " "
        else:
            passString += i
passports.append(passString)

okPass = 0
okPassports = []
for i in passports:
    if "byr:" in i and "iyr:" in i and "eyr:" in i and "hgt:" in i and "hcl:" in i and "ecl:" in i and "pid:" in i:
        okPassports.append(i)
        okPass += 1
print(okPass)

okPass = 0
for i in okPassports:
    y = i.split(" ")
    passCheck = True
    for x in y:
        data = x.split(":")
        if data[0] == "byr":
            if int(data[1]) < 1920 or int(data[1]) > 2002:
                passCheck = False
                break
        elif data[0] == "iyr":
            if int(data[1]) < 2010 or int(data[1]) > 2020:
                passCheck = False
                break
        elif data[0] == "eyr":
            if int(data[1]) < 2020 or int(data[1]) > 2030:
                passCheck = False
                break
        elif data[0] == "hgt":
            if "cm" in data[1]:
                length = data[1][0:-2]
                if int(length) < 150 or int(length) > 193:
                    passCheck = False
                    break
            elif "in" in data[1]:
                length = data[1][0:-2]
                if int(length) < 59 or int(length) > 76:
                    passCheck = False
                    break
            else:
                passCheck = False
                break
        elif data[0] == "hcl" :
            if (data[1][0] != "#"):
                passCheck = False
                break
            datatemp = data[1][1:]
            if not re.match('^[1234567890abcdef]+$', datatemp) or len(datatemp) != 6:
                print(data[1])
                passCheck = False
                break
        elif data[0] == "ecl":
            if data[1] == "amb" or data[1] == "blu" or data[1] == "brn" or data[1] == "gry" or data[1] == "grn" or data[1] == "hzl" or data[1] == "oth":
                continue
            else:
                passCheck = False
                break
        elif data[0] == "pid":
            if not data[1].isdigit() or len(data[1]) != 9:
                passCheck = False
                break
    if passCheck:
        okPass += 1

print(okPass)