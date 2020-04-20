def getClockString():
    return input("Часики-то тикают... Чё по Clock'у? Вводи: ")


def getDString():
    return input("Ну-ка чё там по D? Вводи: ")


def printQNQ(clockString, dString):
    arrayQ = []
    arrayNQ = []

    curQ = input("Давай первое значение Q: ")
    curNQ = input("Давай первое значение #Q: ")
    arrayQ.append(curQ)
    arrayNQ.append(curNQ)

    for i in range(1, len(dString)):
        if clockString[i] == "1" and clockString[i - 1] == "0":
            curQ = dString[i - 1]

            if curQ == "1":
                curNQ = "0"
            else:
                curNQ = "1"

            arrayQ.append(curQ)
            arrayNQ.append(curNQ)
        else:
            arrayQ.append(arrayQ[i - 1])
            arrayNQ.append(arrayNQ[i - 1])

    print("Ну посмотри, чё получилось, ё-моё...")
    print("Q: ", end = '')
    for j in arrayQ:
        print(j, end = '')
    print()
    print("#Q: ", end = '')
    for j in arrayNQ:
        print(j, end = '')


def main():
    print("Ща порешаем, ё-моё...")

    clockString = getClockString()
    dString = getDString()

    if len(dString) != len(clockString):
        print("Чёт количество точек не совпадает. Я так работать не буду, иди подумай над своим поведением...")
        return

    printQNQ(clockString, dString)


main()