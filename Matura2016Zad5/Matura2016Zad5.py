def load_data(filename: str) -> list:
    with open(filename, "r") as file:
        return list(map(lambda x: list(x.strip().replace('X', '1').replace('.', '0')), file))


#def extend(data: list) -> list:
#    for line in data:
#        for i in range(50):
#            line.insert(0, '0')
#            line.append('0')
#    for i in range(50):
#        data.insert(0, ['0'] * len(data[1]))
#        data.append(['0'] * len(data[1]))


def copy(data: list) -> list:
    temp = []
    for line in data:
        temp.append(line[:])
    return temp


def neighbours_count(data: list, line: int, i: int) -> int:
    n = len(data[0])
    m = len(data)
    return int(data[line][i-1]) + int(data[line][(i+1)%n]) + int(data[line-1][i-1]) + int(data[line-1][i]) + \
           int(data[line-1][(i+1)%n]) + int(data[(line+1)%m][i-1]) + int(data[(line+1)%m][i]) + int(data[(line+1)%m][(i+1)%n])


def update(data: list) -> list:
    temp = copy(data)
    for line in range(len(data)):
        for i in range(len(data[line])):
            neighbours = neighbours_count(data, line, i)
            if neighbours == 3 or (neighbours == 2 and data[line][i] == '1'):
                temp[line][i] = '1'
            else:
                temp[line][i] = '0'
    return temp


def equal(data_1: list, data_2: list) -> bool:
    for num_1, num_2 in zip(data_1, data_2):
        for i in range(len(num_1)):
            if num_1[i] != num_2[i]:
                return False
    return True


def zad_1(data: list) -> int:
    i = 0
    while i < 37:
        data = update(data)
        i += 1
    #print(data)
    return neighbours_count(data, 1, 18)


def zad_2(data: list) -> int:
    return sum([line.count('1') for line in update(data)])


def zad_3(data: list) -> dict:
    gen = 2
    gen_1 = data
    gen_2 = update(copy(gen_1))
    while equal(gen_1, gen_2) == False:
        gen_1 = copy(gen_2)
        gen_2 = update(gen_2)
        gen += 1
    return {"Generacja": gen, "Zywe komorki": sum([line.count('1') for line in gen_2])}


if __name__ == '__main__':
    data = load_data("gra.txt")
    #extend(data)
    print(zad_1(copy(data)))
    print(zad_2(copy(data)))
    print(zad_3(copy(data)))