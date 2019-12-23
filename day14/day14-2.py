import re
import math

reactions = open("./input.txt", "r").read().split("\n")

conversions = dict()
excess = dict()

for reaction in reactions:
    reaction_formatted = [x.strip() for x in reaction.split("=>")[::-1]]
    inputElements = []
    for reaction_out in [x.strip() for x in reaction_formatted[1].split(",")]:
        inputElements.append(
            (reaction_out.split(" ")[1], reaction_out.split(" ")[0]))
    conversions[reaction_formatted[0].split(" ")[1]] = (
        int(reaction_formatted[0].split(" ")[0]), inputElements)


fuel_requirements = conversions["FUEL"]


def calc(n, item, waste):
    if item == "ORE":
        return (n, waste)
    else:
        if not item in waste:
            waste[item] = 0
        (nget, need) = conversions[item]
        while n > 0 and waste[item] > 0:
            n -= 1
            waste[item] -= 1
        batches = (math.ceil(n/nget))
        made = batches * nget
        leftovers = made-n
        waste[item] += leftovers
        ans = 0
        for (ny, y) in need:
            (val, w) = calc(int(y) * batches, ny, waste)
            ans += val
            waste = w
        return (ans, waste)


counter = 1
oldCounter = 0
while counter != oldCounter:
    oldCounter = counter
    ore = 0
    log = 1
    while ore < 1000000000000:
        waste = dict()
        ore = calc(counter, "FUEL", waste)[0]
        if ore >= 1000000000000:
            break
        log *= 2
        counter += log
    counter = counter - log
print(counter)
