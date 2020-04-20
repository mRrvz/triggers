from rs_nor1 import rs_nor
from rs_nand2 import rs_nand
from onestep_rs_nand3 import onestep_rs_nand
from twostep_rs_nand4 import twostep_rs_nand
from twostep_jk_nand5 import twostep_jk_nand
from syn_d_nand6 import syn_d_nand
from dyn_d_nand7 import dyn_d_nand


def print_commands():
    print("\n1. Асинхронный RS триггер на элементах ИЛИ-НЕ")
    print("2. Асинхронный RS триггер на элементах И-НЕ")
    print("3. Синхронный одноступенчатый RS триггер на элементах И-НЕ")
    print("4. Синхронный двухступенчатый RS триггер на элементах И-НЕ")
    print("5. Синхронный двухступенчатый JK триггер на элементах И-НЕ")
    print("6. Синхронный двухступенчатый D триггер на элементах И-НЕ")
    print("7. Динамический D триггер")
    print("8. Выйти")


def main():
    menu = {
        "1": rs_nor,
        "2": rs_nand,
        "3": onestep_rs_nand,
        "4": twostep_rs_nand,
        "5": twostep_jk_nand,
        "6": syn_d_nand,
        "7": dyn_d_nand,
        "8": exit
    }

    while True:
        print_commands()
        action = input("Введите номер: ")

        if action not in menu:
            print("Такого пункта нет в меню")
        else:
            trigger_func = menu.get(action)

        trigger_func()


if __name__ == "__main__":
    main()
