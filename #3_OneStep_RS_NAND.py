from trigger_reader import get3, signal_to_string

def getClockString():
    return input("Часики-то тикают... Чё по Clock'у? Вводи: ")

def getResetString():
    return input("Ну-ка чё там по Reset'у? Вводи: ")


def getSetString():
    return input("Во дают. А чё там по Set'у? Вводи: ")


def printQNQ(clockString, setString, resetString):
    arrayQ = []
    arrayNQ = []

    if setString[0] == "0" and resetString[0] == "0" or clockString[0] == "0":
        print("Браток, я чёт не понял, я как тебе должен хранение первое определить?\n"
              "У бабушки Ванги пойду узнаю, ты пока перезапусти с нормальынми данными...")
        return

    for i in range(len(resetString)):
        if clockString[i] == "1":
            if resetString[i] == "1" and setString[i] == "0":
                arrayQ.append(0)
                arrayNQ.append(1)
            elif resetString[i] == "0" and setString[i] == "1":
                arrayQ.append(1)
                arrayNQ.append(0)
            elif resetString[i] == "1" and setString[i] == "1":
                arrayQ.append(1)
                arrayNQ.append(1)
            else:
                if resetString[i - 1] == "1" and setString[i - 1] == "1" and clockString[i - 1] != "0":
                    arrayQ.append("X")
                    arrayNQ.append("X")
                else:
                    arrayQ.append(arrayQ[i - 1])
                    arrayNQ.append(arrayNQ[i - 1])
        else:
            if resetString[i - 1] == "1" and setString[i - 1] == "1" and clockString[i - 1] != "0":
                arrayQ.append("X")
                arrayNQ.append("X")
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

    clockString, resetString, setString = get3()
    print("Clock: ", signal_to_string(clockString))
    print("Reset: ", signal_to_string(resetString))
    print("Set: ", signal_to_string(setString))

    if len(resetString) != len(setString) or len(clockString) != len(resetString):
        print("Чёт количество точек не совпадает. Я так работать не буду, иди подумай над своим поведением...")
        return

    printQNQ(clockString, setString, resetString)


if __name__ == "__main__":
    main()
