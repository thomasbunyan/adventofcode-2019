import re
import math
data = list(map(lambda x: {"pos": list(map(int, re.sub("([< >a-z=])", "", x).split(
    ","))), "vel": [0, 0, 0]}, open("./input.txt", "r").read().split("\n")))


def main():
    lcm = _lcm(_lcm(simulate("x"), simulate("y")), simulate("z"))
    print(lcm)


def simulate(dimension):
    if dimension == "x":
        dataSet = list(map(lambda x: [x["pos"][0],  x["vel"][0]], data))
    if dimension == "y":
        dataSet = list(map(lambda x: [x["pos"][1],  x["vel"][1]], data))
    if dimension == "z":
        dataSet = list(map(lambda x: [x["pos"][2],  x["vel"][2]], data))
    e = 1
    i = 0
    while e != 0:
        applyGravity(dataSet)
        e = getEnergy(dataSet)
        i += 1
    return i


def applyGravity(planets):
    for planet in planets:
        for planetComp in planets:
            if planet[0] > planetComp[0]:
                planet[1] += -1
            elif planet[0] < planetComp[0]:
                planet[1] += 1
    for planet in planets:
        planet[0] += planet[1]


def getEnergy(planets):
    total = 0
    for planet in planets:
        total += abs(planet[0]) * abs(planet[1])
    return total


def _lcm(a, b):
    return a * b // math.gcd(a, b)


main()
