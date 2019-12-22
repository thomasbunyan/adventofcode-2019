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
        return n
    else:
        ans = 0
        (nget, need) = conversions[item]
        print("Need:", n, "of", item)
        batches = (math.ceil(n/nget))
        made = batches * nget
        print(item, batches, "reaction will produce:", made)
        print("Leftovers:", made-n, "\n")
        for (ny, y) in need:
            ans += batches*calc(int(y), ny, waste)
        return ans


print(calc(1, "FUEL"), dict())


# def calc(req, required, waste2):
#     inputs = req["input"]
#     if inputs[0][0] == "ORE":
#         # print(required)
#         if not required[0] in waste2:
#             waste2[required[0]] = 0
#         ores = waste2[required[0]]
#         ore_val = int(req["input"][0][1])
#         i = 0
#         while ores < required[1]:
#             ores += int(req["out_amount"])
#             i += 1
#         waste2[required[0]] = ores - required[1]
#         if not "ans" in waste2:
#             waste2["ans"] = 0
#         waste2["ans"] += i * ore_val
#         # print(i * ore_val)
#         # print(waste2)
#         return waste2

#     for i in inputs:
#         element = i[0]
#         amount = int(req["out_amount"])
#         e_yield = int(i[1]) * amount
#         # print(element, e_yield, amount, e_yield * amount, required[1])
#         # e_yield *= required[1]
#         print(e_yield, required[1])
#         counter = 0
#         while e_yield < required[1]:
#             e_yield += (int(i[1]) * amount)
#             counter += 1
#         print(e_yield, required[1])

#         waste2 = calc(conversions[[i][0][0]], (element,  e_yield), waste2)

#     return waste2
