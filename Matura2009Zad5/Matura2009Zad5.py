def load_data(filename: str) -> list:
    with open(filename, "r") as file:
        return list(map(lambda x: x.strip().split(), file))


def write_to_file(filename: str, data):
    with open(filename, "a") as file:
        if isinstance(data, list):
            file.writelines([word+'\n' for word in data])
        else:
            file.write(str(data)+'\n')


def clear_file(filename: str):
    with open(filename, "w") as file:
        file.write("")


def palindromes(data: list):
    palindrome_sum = sum(1 for word in data if word[0] == word[0][::-1])
    palindrome_sum += sum(1 for word in data if word[1] == word[1][::-1])
    write_to_file("zad_5.txt", palindrome_sum)


def b_inside_a(data: list):
    counter = sum(1 for word in data if word[1] in word[0])
    write_to_file("zad_5.txt", counter)


def stick_them(data: list):
    counter = 0
    for words in data:
        if words[1] in words[0]:
            continue
        found = False
        for i in range(len(words[1]), 0, -1):
            if words[0][-i:] == words[1][:i] or words[1][-i:] == words[0][:i]:
                found = True
                break
        if found == False:
            counter += 1
    write_to_file("zad_5.txt", counter)


def shortest_c(data: list):
    word_list = []
    for words in data:
        if words[1] in words[0]:
            word_list.append(words[0])
            continue
        found = False
        for i in range(len(words[1]), 0, -1):
            if words[0][-i:] == words[1][:i]:
                word_list.append(words[0][:-i] + words[1])
                found = True
                break
            if words[1][-i:] == words[0][:i]:
                word_list.append(words[1][:-i] + words[0])
                found = True
                break
        if found == False:
            word_list.append(words[0] + words[1])
    write_to_file("slowa.txt", word_list)


if __name__ == '__main__':
    data = load_data("dane.txt")
    clear_file("zad_5.txt")
    clear_file("slowa.txt")
    palindromes(data)
    b_inside_a(data)
    stick_them(data)
    shortest_c(data)