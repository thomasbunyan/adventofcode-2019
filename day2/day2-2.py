f = open("./input.txt", "r")
data = list(map(int, f.read().split(",")))
data[1] = 0
data[2] = 0


def getOutput(data):
    for x in range(0, len(data), 4):
        if data[x] == 1:
            data[data[x+3]] = data[data[x + 2]] + \
                data[data[x + 1]]
        elif data[x] == 2:
            data[data[x+3]] = data[data[x + 2]] * \
                data[data[x + 1]]
        elif data[x] == 99:
            return data[0]


def main(target):
    noun = 0
    verb = 0
    while noun <= 99:
        val = getOutput(data.copy())
        if val == target:
            break
        elif val < target:
            noun = noun + 1
            data[1] = noun
        elif val > target:
            noun = noun - 1
            data[1] = noun
            break
    while verb <= 99:
        val = getOutput(data.copy())
        if val == target:
            break
        elif val < target:
            verb = verb + 1
            data[2] = verb
    print(100 * noun + verb)


main(19690720)
