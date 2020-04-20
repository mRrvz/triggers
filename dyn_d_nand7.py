from trigger_reader import get2, signal_to_string

def getClockString():
    return input("Часики-то тикают... Чё по Clock'у? Вводи: ")


def getDString():
    return input("Ну-ка чё там по D? Вводи: ")


def printQNQ(clockString, dString, curQ, curNQ):
    arrayQ = []
    arrayNQ = []

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


def dyn_d_nand():
    print("Ща порешаем, ё-моё...")

    clockString, dString, q, nq = get2(False)
    print("Clock: ", signal_to_string(clockString))
    print("D: ", signal_to_string(dString))
    print("Q: ", signal_to_string(q))
    print("#Q: ", signal_to_string(nq))

    if len(dString) != len(clockString):
        print("Чёт количество точек не совпадает. Я так работать не буду, иди подумай над своим поведением...")
        return

    printQNQ(clockString, dString, q, nq)

if __name__ == "__main__":
    dyn_d_nand()
