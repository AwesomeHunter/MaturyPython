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
    maxi = -1
    lens = []
    for number in data:
        temp_len = len(max(number.split('1'), key=len))
        if temp_len >= maxi:
            lens.append((number, temp_len))
        maxi = max(maxi, temp_len)
    return {
        "list_of_longest": [num[0] for num in lens if num[1] == maxi],
        "max_len": maxi
    }


if __name__ == '__main__':
    data = load_data("slowa.txt")
    print(zad_1(data))
    print(zad_2(data))
    zad_3_ans = zad_3(data)
    print('\n'.join(zad_3_ans["list_of_longest"]))
    print(zad_3_ans["max_len"])
