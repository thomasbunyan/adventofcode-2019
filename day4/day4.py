def main(input):
    counter = 0
    minVal = int(input.split("-")[0])
    maxVal = int(input.split("-")[1])
    for x in range(minVal, maxVal):
        if(checkOrder(x) and checkDouble(x)):
            counter = counter + 1
    print(counter)


def checkOrder(num):
    num = str(num)
    for i in range(1, len(num)):
        if(int(num[i - 1]) > int(num[i])):
            return False
    return True


def checkDouble(num):
    num = str(num)
    for i in range(0, len(num) - 1):
        if num[i] == num[i + 1]:
            return True
    return False


main("265275-781584")
