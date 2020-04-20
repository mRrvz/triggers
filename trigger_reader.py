from functools import reduce

def signal_to_string(signal):
    return reduce(lambda x, y: x + y, signal)

def parse_url(url):
    url = url[url.find('wave%'):]
    return url[url.find("'") + 1:]


def parse_signal(trigger):
    signal = []

    i = 0
    while trigger[i] != "'":
        if trigger[i].isdigit() or trigger[i] == 'h' or trigger[i] == 'l':
            signal.append(trigger[i])
        else:
            signal.append(signal[-1])

        i += 1

    if 'h' in signal:
        signal = list(map(lambda x: '1' if x == 'h' else '0', signal))

    return signal


def get2():
    url = parse_url(input('Введите ссылку на триггер: '))
    first = parse_signal(url)
    second = parse_signal(parse_url(url))

    return first, second


def get3():
    url = parse_url(input('Введите ссылку на триггер: '))
    first = parse_signal(url)
    url = parse_url(url)
    second = parse_signal(url)
    third = parse_signal(parse_url(url))

    return first, second, third
