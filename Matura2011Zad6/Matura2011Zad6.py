def load_data(filename: str) -> list:
    with open(filename, "r") as file:
        return list(map(str.strip, file))


def clear_file():
    with open("zadanie6.txt", "w") as ans:
        ans.write("")


def write_to_file(filename: str, data: int):
    with open(filename, "a") as file:
        file.write(str(data) + '\n')


def even_nums(data: list):
    write_to_file("zadanie6.txt", sum([1 for num in data if num[-1] == '0']))


def biggest(data: list):
    biggest_num = sorted(data, key = lambda x: int(x, 2))[-1]
    write_to_file("zadanie6.txt", biggest_num)
    write_to_file("zadanie6.txt", int(biggest_num, 2))


def sum_all_9_dig(data: list):
    write_to_file("zadanie6.txt", sum([1 for num in data if len(num) == 9]))
    write_to_file("zadanie6.txt", bin(sum([int(num, 2) for num in data if len(num) == 9]))[2:])


if __name__ == '__main__':
    data = load_data("liczby.txt")
    clear_file()
    even_nums(data)
    biggest(data)
    sum_all_9_dig(data)