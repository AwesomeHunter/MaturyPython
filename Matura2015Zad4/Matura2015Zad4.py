def load_data(filename: str) -> list:
    with open(filename, "r") as file:
        return list(map(str.strip, file))


def zad_1(data: list) -> int:
    return sum(1 for num in data if num.count('0') > len(num)//2)


def zad_2(data: list) -> int:
    ans = 0
    for num in data:
        pom = 0
        while num[pom] == '0' and pom < len(num) - 1:
            pom += 1
        if pom == 0:
            continue
        if pom + num.count('1') == len(num):
            ans += 1
    return ans


def zad_3(data: list) -> list:
    max_len = max([len(max(num.split('1'), key = len)) for num in data])
    return [num for num in data if len(max(num.split('1'), key = len)) == max_len], max_len


if __name__ == '__main__':
    data = load_data("slowa.txt")
    print(zad_1(data))
    print(zad_2(data))
    zad_3_ans, zad_3_len = zad_3(data)
    print('\n'.join(zad_3_ans))
    print(zad_3_len)