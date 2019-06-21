def load_data(filename: str, filename_2: str) -> list:
    with open(filename, "r") as file, open(filename_2, "r") as file_2:
        return list(zip(map(str.strip, file), map(str.strip, file_2)))


def write_to_file(filename: str, data: list):
    with open(filename, "w") as file:
        file.writelines([word + '\n' for word in data])


def code(data: list):
    coded = []
    for word in data:
        ans = ""
        for i in range(len(word[0])):
            if ord(word[0][i]) + ord(word[1][i % (len(word[1]))]) - 64 > 90:
                ans += chr(ord(word[0][i]) + ord(word[1][i % (len(word[1]))]) - 64 - 26)
            else:
                ans += chr(ord(word[0][i]) + ord(word[1][i % (len(word[1]))]) - 64)
        coded.append(ans)
    write_to_file("wynik4a.txt", coded)


def decode(data: list):
    decoded = []
    for word in data:
        ans = ""
        for i in range(len(word[0])):
            if ord(word[0][i]) - ord(word[1][i % (len(word[1]))]) + 64 < 65:
                ans += chr(ord(word[0][i]) - ord(word[1][i % (len(word[1]))]) + 64 + 26)
            else:
                ans += chr(ord(word[0][i]) - ord(word[1][i % (len(word[1]))]) + 64)
        decoded.append(ans)
    write_to_file("wynik4b.txt", decoded)


if __name__ == '__main__':
    data_1 = load_data("tj.txt", "klucze1.txt")
    data_2 = load_data("sz.txt", "klucze2.txt")
    code(data_1)
    decode(data_2)