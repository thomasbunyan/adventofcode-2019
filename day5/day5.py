f = open("./input.txt", "r")
data = list(map(int, f.read().split(",")))


def main():
    toSkip = False
    for x in range(0, len(data), 2):
        if toSkip:
            toSkip = False
            continue

        opcode = getCode(data[x])
        if opcode[3] == 1 or opcode[3] == 2:
            if opcode[2]:
                val1 = data[x + 1]
            else:
                val1 = data[data[x + 1]]
            if opcode[1]:
                val2 = data[x + 2]
            else:
                val2 = data[data[x + 2]]

        if opcode[3] == 1:
            data[data[x+3]] = val1 + val2
            toSkip = True
        elif opcode[3] == 2:
            data[data[x+3]] = val1 * val2
            toSkip = True
        elif opcode[3] == 3:
            data[data[x+1]] = int(input("Enter a value: "))
        elif opcode[3] == 4:
            print(data[data[x+1]])
        elif opcode[3] == 99:
            exit()


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
