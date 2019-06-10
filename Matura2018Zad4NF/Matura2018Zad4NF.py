def load_data(filename: str) -> list:
    with open(filename + ".txt", "r") as file:
        return list(map(str.strip, file))


def clear_file():
    with open("wyniki4.txt", "w") as ans:
        ans.write("")


def find_hidden_word(data: list) -> str:
    with open("wyniki4.txt", "a") as ans:
        ans.write(''.join([data[word][9] for word in range(39, len(data), 40)]) + '\n')


def max_unique(data: list) -> str:
    maxi_word = data[0]
    for word in data:
        if len(set(maxi_word)) < len(set(word)):
            maxi_word = word
    with open("wyniki4.txt", "a") as ans:
        ans.write(maxi_word + " " + str(len(set(maxi_word))) + '\n')


def find_words(data: list) -> list:
    with open("wyniki4.txt", "a") as ans:
        ans.write('\n'.join([word for word in data if abs(ord(''.join(sorted(word))[0]) - ord(''.join(sorted(word))[-1])) <= 10]))


if __name__ == '__main__':
    data = load_data("sygnaly")
    clear_file()
    find_hidden_word(data)
    max_unique(data)
    find_words(data)