from itertools import chain, permutations


def main():
    maxSignal = 0
    phaseSetting = None
    for phase in permutations([0, 1, 2, 3, 4]):
        res = amp(phase)
        if res > maxSignal:
            maxSignal = res
            phaseSetting = phase
    return ((maxSignal, phaseSetting))


def amp(phaseSetting):
    out = intcode([phaseSetting[0], 0])
    for x in range(1, 5):
        out.insert(0, phaseSetting[x])
        out = intcode(out)
    return out[0]


opcodeDict = {1: 'rrw', 2: 'rrw', 3: 'w', 4: 'r',
              5: 'rr', 6: 'rr', 7: 'rrw', 8: 'rrw',
              99: ''}


def intcode(input_list):
    f = open("./input.txt", "r")
    data = list(map(int, f.read().split(",")))
    index = 0
    output = []
    while True:
        paramMode = getCode(data[index])
        opcode = paramMode[0]
        args = getArgs(data, paramMode, opcode, index)
        # print("Opcode", opcode)
        # print(args)
        if opcode == 1:
            data[args[2]] = args[0] + args[1]
        elif opcode == 2:
            data[args[2]] = args[0] * args[1]
        elif opcode == 3:
            if input_list == []:
                inp = int(input("Enter a value: "))
            else:
                # inp = next(iter(input_list))
                inp = input_list[0]
                input_list.pop(0)
            data[args[0]] = inp
        elif opcode == 4:
            output.append(args[0])
            # yield output
        elif opcode == 5:
            if args[0] != 0:
                index = args[1]
                continue
        elif opcode == 6:
            if args[0] == 0:
                index = args[1]
                continue
        elif opcode == 7:
            if args[0] < args[1]:
                data[args[2]] = 1
            else:
                data[args[2]] = 0
        elif opcode == 8:
            if args[0] == args[1]:
                data[args[2]] = 1
            else:
                data[args[2]] = 0
        elif opcode == 99:
            break
        else:
            print("Bad opcode")
        index += len(opcodeDict[opcode]) + 1
    return output


def getCode(opcode):
    if opcode < 100:
        return (opcode, 0, 0, 0)
    elif opcode < 1000:
        return (int(str(opcode)[1] + str(opcode)[2]), int(str(opcode)[0]), 0, 0)
    elif opcode < 10000:
        return (int(str(opcode)[2] + str(opcode)[3]), int(str(opcode)[1]), int(str(opcode)[0]), 0)
    else:
        return (int(str(opcode)[3] + str(opcode)[4]), int(str(opcode)[2]), int(str(opcode)[1]), int(str(opcode)[0]))


def getArgs(data, paramMode, opcode, index):
    args = []
    for i in range(0, len(opcodeDict[opcode])):
        if opcodeDict[opcode][i] == "r":
            if paramMode[i + 1] == 1:
                args.append(int(data[index + i + 1]))
            elif paramMode[i + 1] == 0:
                args.append(int(data[data[index + i + 1]]))
        elif opcodeDict[opcode][i] == "w":
            args.append(int(data[index + i + 1]))
    return args


print(main())
# intcode([])
