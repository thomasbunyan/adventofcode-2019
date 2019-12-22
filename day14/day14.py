import re

reactions = open("./input.txt", "r").read().split("\n")

conversions = dict()
excess = dict()

for reaction in reactions:
    reaction_formatted = [x.strip() for x in reaction.split("=>")[::-1]]
    inputElements = []
    for reaction_out in [x.strip() for x in reaction_formatted[1].split(",")]:
        inputElements.append(
            (reaction_out.split(" ")[1], reaction_out.split(" ")[0]))
    conversions[reaction_formatted[0].split(" ")[1]] = {
        "out_amount": reaction_formatted[0].split(" ")[0], "input": inputElements}


fuel_requirements = conversions["FUEL"]
# print(fuel_requirements)


def calc(req, required, waste2):
    inputs = req["input"]
    if inputs[0][0] == "ORE":
        if not required[0] in waste2:
            waste2[required[0]] = 0
        ores = waste2[required[0]]
        ore_val = int(req["input"][0][1])
        i = 0
        while ores < required[1]:
            ores += int(req["out_amount"])
            i += 1
        waste2[required[0]] = ores - required[1]
        if not "ans" in waste2:
            waste2["ans"] = 0
        waste2["ans"] += i * ore_val
        # print(waste2)
        return waste2

    for i in inputs:
        element = i[0]
        e_yield = int(i[1])
        amount = int(req["out_amount"])
        print(element, e_yield, amount)
        e_yield *= required[1]
        waste2 = calc(conversions[[i][0][0]], (element, e_yield), waste2)

    return waste2


print(calc(fuel_requirements, ("FUEL", 1), dict())["ans"])
