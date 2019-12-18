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
    if o in orbits.keys():
        innerCounter = 0
        for x in orbits[o]:
            innerCounter = innerCounter + getLength(x, counter + 1)
        return counter + innerCounter
    else:
        return counter


addOrbits()
print(getLength("COM", 0))
