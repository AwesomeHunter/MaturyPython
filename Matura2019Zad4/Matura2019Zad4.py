def load_data(filename: str) -> list:
    with open(filename, 'r') as file:
        data = []
        pom = []
        for line in file:
            if line == '\n':
                data.append(pom)
                pom = []
            else:
                pom.append(line.strip())
    return data


def reverse(area: list) -> list:
    copy_area = []
    for line in area:
        copy_area.append(line[:])
    for i in range(len(copy_area)//2):
        copy_area[i], copy_area[29 - i] = copy_area[29 - i][::-1], copy_area[i][::-1]
    return copy_area


def check_area(area: list, line: int = 0) -> int:
    if line == 30:
        return 30
    for i in range(line + 1):
        if area[i][line] == 'X':
            return line
    for i in range(line + 1):
        if area[line][i] == 'X':
            return line
    return check_area(area, line + 1)


def zad_1(data: list) -> int:
    return sum([1 for area in data if sum([line.count('*') for line in area]) / 900 >= 0.7])


def zad_2(data: list) -> list:
    for area_num in range(len(data)):
        reversed_area = reverse(data[area_num])
        for i in range(area_num + 1, len(data)):
            if reversed_area == data[i]:
                return [area_num + 1, i + 1]


def zad_3(data: list) -> dict:
    area_list = [(check_area(area), i + 1) for i, area in enumerate(data)]
    max_size = max(area_list)[0]
    return {'Dl. boku:': max_size, 'Numery:': [pair[1] for pair in area_list if pair[0] == max_size]}


if __name__ == '__main__':
    data = load_data('dzialki.txt')
    print(zad_1(data))
    print(zad_2(data))
    print(zad_3(data))