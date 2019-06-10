def load_data(filename: str) -> dict:
    data = []
    data_2 = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip().split()
            line = [int(i) for i in line]
            for i in range(len(line)):
                if len(data)-1 < i:
                    data.append([])
                data[i].append(line[i])
            data_2.append(line)
    return [data, data_2]


def min_max(data_list: list) -> dict:
    mini = 300
    maxi = -1
    for i in data_list:
        mini = min(min(i), mini)
        maxi = max(max(i), maxi)
    return [mini, maxi]


def symmetry(data_list: list) -> int:
    return sum([1 for i in data_list if i != i[::-1]])


def pixels_line(data_list: list) -> int:
    maxi_num = 0
    for line in data_list:
        current_num = 1
        for i in range(len(line)-1):
            if line[i] == line[i+1]:
                current_num += 1
            else:
                maxi_num = max(current_num, maxi_num)
                current_num = 1
    return maxi_num


def neighbours(data_list: list) -> int:
    neighbours_counter = 0
    for i in data_list:
        i.append(-1)
        i.insert(0, -1)
    data_list.insert(0, [-1] * len(data_list[1]))
    data_list.append([-1] * len(data_list[1]))
    for line in range(1, len(data_list)-1):
        for i in range(1, len(data_list[line])-1):
            if (abs(data_list[line][i] - data_list[line][i - 1]) > 128 and data_list[line][i - 1] != -1) \
            or (abs(data_list[line][i] - data_list[line][i + 1]) > 128 and data_list[line][i + 1] != -1) \
            or (abs(data_list[line][i] - data_list[line + 1][i]) > 128 and data_list[line + 1][i] != -1) \
            or (abs(data_list[line][i] - data_list[line - 1][i]) > 128 and data_list[line - 1][i] != -1):
                neighbours_counter += 1
    return neighbours_counter


if __name__ == '__main__':
    loaded_data, loaded_data_2 = load_data("dane.txt")
    mini, maxi = min_max(loaded_data)
    print("Minimalna wartosc: ", mini)
    print("Maksymalna wartosc: ", maxi)
    print("By byla symetria, trzeba usunac: ", symmetry(loaded_data_2)," wierszy")
    print("Najdluzszy ciag pikseli o tej samej jasnosci: ", pixels_line(loaded_data))
    print("Ilosc sasiadujacych, kontrastujacych pikseli: ", neighbours(loaded_data))