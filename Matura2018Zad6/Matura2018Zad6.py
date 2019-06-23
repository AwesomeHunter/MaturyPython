from collections import Counter

def load_data(filename: str) -> list:
    with open(filename, "r") as file:
        return list(map(lambda x: list(x.strip().split()), file))


def zad_1(data: list) -> int:
    return sum([1 for word in data if word[0][-1] == 'A']) + sum([1 for word in data if word[1][-1] == 'A'])


def zad_2(data: list) -> int:
    return sum([1 for word in data if word[0] in word[1]])


def zad_3(data: list) -> dict:
    words = [pair for pair in data if Counter(pair[0]) == Counter(pair[1])]
    return {'Amount:': len(words), 'Pairs:': words}


if __name__ == '__main__':
    data = load_data('slowa.txt')
    print(zad_1(data))
    print(zad_2(data))
    print(zad_3(data))