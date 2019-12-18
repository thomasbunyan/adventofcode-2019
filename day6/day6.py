f = open("./input.txt", "r")
data = f.read().split("\n")

orbits = dict()


def addOrbits():
    for x in data:
        left = x.split(")")[0]
        right = x.split(")")[1]
        if left in orbits.keys():
            orbits[left].append(right)
        else:
            orbits[left] = [right]


def getLength(o, counter):
    innerCounter = 0
    if o in orbits.keys():
        for x in orbits[o]:
            innerCounter = innerCounter + getLength(x, counter + 1)
    return counter + innerCounter


addOrbits()
print(getLength("COM", 0))
