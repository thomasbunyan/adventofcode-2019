import re

data = list(map(lambda x: {"pos": list(
    map(int, re.sub("([< >a-z=])", "", x).split(","))), "vel": [0, 0, 0]}, open("./input.txt", "r").read().split("\n")))


def main():
    simulate(10)


def simulate(iterations):
    for x in range(iterations):
        applyGravity(data)
        applyVelocity(data)
    print(getEnergy(data))


def applyGravity(planets):
    for planet in planets:
        for planetComp in planets:
            if planet["pos"] == planetComp["pos"]:
                pass
            for i in range(3):
                if planet["pos"][i] > planetComp["pos"][i]:
                    planet["vel"][i] += -1
                elif planet["pos"][i] < planetComp["pos"][i]:
                    planet["vel"][i] += 1


def applyVelocity(planets):
    for planet in planets:
        for i in range(3):
            planet["pos"][i] += planet["vel"][i]


def getEnergy(planets):
    pot = []
    kin = []
    total = []
    for planet in planets:
        pot.append(abs(planet["pos"][0]) +
                   abs(planet["pos"][1]) + abs(planet["pos"][2]))
        kin.append(abs(planet["vel"][0]) +
                   abs(planet["vel"][1]) + abs(planet["vel"][2]))
    for i in range(len(pot)):
        total.append(pot[i] * kin[i])
    return sum(total)


main()
