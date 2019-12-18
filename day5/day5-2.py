f = open("./input.txt", "r")
data = list(map(int, f.read().split(",")))


def main():
    toSkip = False
    x = 0
    while x < len(data):
        opcode = getCode(data[x])
        val1 = getVal(opcode, x, 1)
        val2 = getVal(opcode, x, 2)
        val3 = getVal(opcode, x, 3)

        if opcode[3] == 1:
            data[val3] = val1 + val2
            x = x + 4
        elif opcode[3] == 2:
            data[val3] = val1 * val2
            x = x + 4
        elif opcode[3] == 3:
            data[data[x+1]] = int(input("Enter a value: "))
            x = x + 2
        elif opcode[3] == 4:
            print(val1)
            x = x + 2
        elif opcode[3] == 5:
            if val1 != 0:
                x = val2
            else:
                x = x + 3
        elif opcode[3] == 6:
            if val1 == 0:
                x = val2
            else:
                x = x + 3
        elif opcode[3] == 7:
            if val1 < val2:
                data[val3] = 1
            else:
                data[val3] = 0
            x = x + 4
        elif opcode[3] == 8:
            if val1 == val2:
                data[val3] = 1
            else:
                data[val3] = 0
            x = x + 4
        elif opcode[3] == 99:
            exit()


def getVal(opcode, x, val):
    try:
        if val == 1:
            if opcode[2] == 0:
                return data[data[x + 1]]
            else:
                return data[x + 1]
        elif val == 2:
            if opcode[1] == 0:
                return data[data[x + 2]]
            else:
                return data[x + 2]
        elif val == 3:
            return data[x + 3]

    except:
        return


def getCode(opcode):
    if opcode < 100:
        return (0, 0, 0, opcode)
    elif opcode < 1000:
        return (0, 0, int(str(opcode)[0]), int(
            str(opcode)[1] + str(opcode)[2]))
    elif opcode < 10000:
        return (0, int(str(opcode)[0]), int(str(opcode)[1]), int(
            str(opcode)[2] + str(opcode)[3]))
    else:
        return (int(str(opcode)[0]), int(str(opcode)[1]), int(str(opcode)[2]), int(
            str(opcode)[3] + str(opcode)[4]))


main()
