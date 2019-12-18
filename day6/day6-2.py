f = open("./input.txt", "r")
data = f.read().split("\n")

orbits = dict()
distance = dict()


def addOrbits():
    for x in data:
        left = x.split(")")[0]
        right = x.split(")")[1]
        if left in orbits.keys():
            orbits[left].append(right)
        else:
            orbits[left] = [right]
        if right in orbits.keys():
            orbits[right].append(left)
        else:
            orbits[right] = [left]


def dijkstra(o, dis):
    if len(distance) >= len(orbits) or o in distance.keys():
        return
    distance[o] = dis
    for x in orbits[o]:
        dijkstra(x, dis + 1)


addOrbits()
dijkstra("YOU", 0)
print(distance["SAN"] - 2)
