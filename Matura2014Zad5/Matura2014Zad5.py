# dlamaturzysty.info/s/1625/36234-Matura-arkusze-maturalne/133033-Informatyka-poziom-rozszerzony-matura-2014-pytania-i-odpowiedzi.htm

from collections import Counter

def load_data(filename: str) -> list:
    with open(filename, "r") as file:
        return list(map(str.strip, file))


def is_prime(x: int) -> bool:
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


def zad_1(data: list) -> int:
    return sum([1 for word in data if is_prime(sum([ord(i) for i in word]))])


def zad_2(data: list) -> list:
    increasing = []
    for word in data:
        good = True
        for i in range(1, len(word)):
            if ord(word[i-1]) >= ord(word[i]):
                good = False
                break
        if good:
            increasing.append(word)
    return increasing


def zad_3(data: list) -> list:
    return [item for item, count in Counter(data).items() if count > 1]


if __name__ == '__main__':
    data = load_data("NAPIS.txt")
    print(zad_1(data))
    print(zad_2(data))
    print(zad_3(data))