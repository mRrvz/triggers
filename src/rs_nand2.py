from src.trigger_reader import get2, signal_to_string

def getResetString():
    return input("Ну-ка чё там по Reset'у? Вводи: ")


def getSetString():
    return input("Во дают. А чё там по Set'у? Вводи: ")


def printQNQ(setString, resetString):
    arrayQ = []
    arrayNQ = []

    if setString[0] == "1" and resetString[0] == "1":
        print("Браток, я чёт не понял, я как тебе должен хранение первое определить?\n"
              "У бабушки Ванги пойду узнаю, ты пока перезапусти с нормальынми данными...")
        return

    for i in range(len(resetString)):
        if resetString[i] == "0" and setString[i] == "1":
            arrayQ.append(0)
            arrayNQ.append(1)
        elif resetString[i] == "1" and setString[i] == "0":
            arrayQ.append(1)
            arrayNQ.append(0)
        elif resetString[i] == "0" and setString[i] == "0":
            arrayQ.append(1)
            arrayNQ.append(1)
        else:
            if resetString[i - 1] == "0" and setString[i - 1] == "0":
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


def rs_nand():
    print("Ща порешаем, ё-моё...")

    resetString, setString = get2()
    print("Reset: ", signal_to_string(resetString))
    print("Set: ", signal_to_string(setString))

    if len(resetString) != len(setString):
        print("Чёт количество точек не совпадает. Я так работать не буду, иди подумай над своим поведением...")
        return

    printQNQ(setString, resetString)


if __name__ == "__main__":
    rs_nand()
