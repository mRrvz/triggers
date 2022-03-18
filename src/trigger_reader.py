from functools import reduce
from urllib.parse import unquote

def signal_to_string(signal):
    return reduce(lambda x, y: x + y, signal)


def get2(start_value=True):
    first = input("Введите первый сигнал:")

    second = input("Введите второй сигнал:")

    if start_value:
        return first, second

    q = input("Введите  Q[0]:")
    nq = input("Введите сигнал !Q[0]:")

    return first, second, q, nq


def get3(start_value=True):
    first = input("Введите первый сигнал:")

    second =input("Введите 2 сигнал:")

    third =input("Введите 3 сигнал:")

    if start_value:
        return first, second, third

    q = input("Q[0]: ")
    nq = input("!Q[0]: ")

    return first, second, third, q, nq
