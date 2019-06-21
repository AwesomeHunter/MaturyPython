def load_data(filename: str) -> list:
    with open(filename, "r") as file:
        return list(map(str.strip, file))


def zad_1(data: list) -> int:
    return sum([1 for word in data if word[0] == word[-1]])


def zad_2(data: list) -> int:
    return sum([1 for word in data if str(int(word, 8))[0] == str(int(word, 8))[-1]])


def zad_3(data: list) -> int:
    words = []
    for word in data:
        is_OK = True
        for i in range(1, len(word)):
            if int(word[i-1]) > int(word[i]):
                is_OK = False
                break
        if is_OK:
            words.append(word)
    return words


if __name__ == '__main__':
    data = load_data("dane.txt")
    print(zad_1(data))
    print(zad_2(data))

    nums = zad_3(data)

    print(len(nums))
    print(max(nums, key = lambda x: int(x, 8)))
    print(min(nums, key = lambda x: int(x, 8)))