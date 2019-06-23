def load_data(filename: str) -> list:
    with open(filename, "r") as file:
        return list(map(str.strip, file))


def zad_1(data: list) -> dict:
    nums = [num for num in data if num[:len(num)//2] == num[len(num)//2:]]
    return {'Ilosc:': len(nums), 'Najdluzszy': max(nums, key = len), 'Dlugosc': len(max(nums, key = len))}


def zad_2(data: list) -> dict:
    wrong = []
    for num in data:
        isGood = True
        for i in range(0, len(num), 4):
            if int(num[i:i + 4], 2) > 9:
                isGood = False
                break
        if isGood == False:
            wrong.append(num)
    return {'Amount:': len(wrong), 'Shortest:': len(min(wrong, key = len))}


def zad_3(data: list) -> dict:
    maxi = max([num for num in data if len(num) <= 16], key = lambda x: int(x, 2))
    return {'Bin:': maxi, 'Dec:': int(maxi, 2)}


if __name__ == '__main__':
    data = load_data('binarne.txt')
    print(zad_1(data))
    print(zad_2(data))
    print(zad_3(data))