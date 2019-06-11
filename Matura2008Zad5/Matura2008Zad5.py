def load_data(filename: str) -> list:
    with open(filename, "r") as file:
        return list(map(str.strip, file))


def reverse_passwords(data: list):
    with open("hasla_a.txt", "w") as file:
        file.writelines('\n'.join([word[::-1] for word in data]))


def longest_shortest(data: list) -> list:
    with open("slowa_a.txt", "w") as file:
        file.write(min(data, key = len)[::-1] + " " + str(len(min(data, key = len))))
        file.write('\n')
        file.write(max(data, key = len)[::-1] + " " + str(len(max(data, key = len))))


def create_better_password(password: str) -> str:
    for i in range(len(password), 0, -1):
        if password[:i] == password[:i][::-1]:
            return (password[i:][::-1] + password)


def write_better_passwords(data: list):
    with open("hasla_b.txt", "w") as file:
        file.writelines('\n'.join([create_better_password(word) for word in data]))


def save_another_passwords(data: list):
    with open("slowa_b.txt", "w") as file:
        file.write("1: ")
        file.writelines('\n'.join([create_better_password(word) for word in data if len(create_better_password(word)) == 12]))
        file.write("\n2: ")
        file.write(max([create_better_password(word) for word in data], key = len))
        file.write(" ")
        file.write(min([create_better_password(word) for word in data], key = len))
        file.write("\n3: ")
        file.write(str(sum([len(create_better_password(word)) for word in data])))


if __name__ == "__main__":
    data = load_data("slowa.txt")

    reverse_passwords(data)
    longest_shortest(data)
    write_better_passwords(data)
    save_another_passwords(data)