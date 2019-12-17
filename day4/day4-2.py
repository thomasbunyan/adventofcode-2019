def main(input):
    counter = 0
    minVal = int(input.split("-")[0])
    maxVal = int(input.split("-")[1])
    for x in range(minVal, maxVal):
        if(checkOrder(x) and checkDouble(x)):
            counter = counter + 1
            print(x)
    print(counter)


def checkOrder(num):
    num = str(num)
    for i in range(1, len(num)):
        if(int(num[i - 1]) > int(num[i])):
            return False
    return True


def checkDouble(num):
    num = str(num)
    counter = 0
    inCounter = 0
    for i in range(0, len(num)):
        if inCounter > 0:
            inCounter = inCounter - 1
            continue
        for j in range(i + 1, len(num)):
            if num[i] == num[j]:
                inCounter = inCounter + 1
        if inCounter == 1:
            counter = counter + 1
    return counter > 0


main("265275-781584")
