f = open("./input.txt", "r")
data = list(map(int, f.read().split(",")))
data[1] = 12
data[2] = 2


def main():
    for x in range(0, len(data), 4):
        if data[x] == 1:
            data[data[x+3]] = data[data[x + 2]] + \
                data[data[x + 1]]
        elif data[x] == 2:
            data[data[x+3]] = data[data[x + 2]] * \
                data[data[x + 1]]
        elif data[x] == 99:
            print(data)
            exit()


main()
