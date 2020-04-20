from trigger_reader import get3, signal_to_string

def getClockString():
    return input("Часики-то тикают... Чё по Clock'у? Вводи: ")


def getJString():
    return input("Ну-ка чё там по J? Вводи: ")


def getKString():
    return input("Во дают. А чё там по K? Вводи: ")


def printQNQ(clockString, kString, jString):
    arrayQ = []
    arrayNQ = []

    curQ = input("Давай первое значение Q: ")
    curNQ = input("Давай первое значение #Q: ")
    arrayQ.append(curQ)
    arrayNQ.append(curNQ)

    for i in range(1, len(kString)):
        if clockString[i] == "0" and clockString[i - 1] == "1":
            if jString[i - 1] == "1" and kString[i - 1] == "0":
                curQ = 1
                curNQ = 0
            elif jString[i - 1] == "0" and kString[i - 1] == "1":
                curQ = 0
                curNQ = 1
            elif jString[i - 1] == "1" and kString[i - 1] == "1":
                curQ, curNQ = curNQ, curQ
            else:
                if i == 1:
                    pass
                elif jString[i - 2] == "1" and kString[i - 2] == "0":
                    curQ = 1
                    curNQ = 0
                elif jString[i - 2] == "0" and kString[i - 2] == "1":
                    curQ = 0
                    curNQ = 1
                elif jString[i - 2] == "1" and kString[i - 2] == "1":
                    curQ, curNQ = curNQ, curQ
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

    clockString, jString, kString = get3()
    print("Clock: ", signal_to_string(clockString))
    print("J: ", signal_to_string(jString))
    print("K: ", signal_to_string(kString))

    if len(kString) != len(jString) or len(clockString) != len(jString):
        print("Чёт количество точек не совпадает. Я так работать не буду, иди подумай над своим поведением...")
        return

    printQNQ(clockString, kString, jString)

if __name__ == "__main__":
    main()
