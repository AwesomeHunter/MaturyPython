from collections import Counter

def load_data(filename: str) -> list:
    with open(filename, "r") as file:
        return list(map(lambda x: x.strip().split(), file))


def write_to_file(filename: str, data: list):
    with open(filename, "w") as file:
        file.writelines([' '.join(word)+'\n' for word in data])


def the_same_len(data: list):
    write_to_file("odp_4a.txt", [words for words in data if len(words[0]) == len(words[1]) == len(words[2]) == len(words[3]) == len(words[4])])


def anagrams(data: list):
    write_to_file("odp_4b.txt", [words for words in data if Counter(words[0]) == Counter(words[1]) == Counter(words[2]) == Counter(words[3]) == Counter(words[4])])


if __name__ == '__main__':
    data = load_data("anagram.txt")
    the_same_len(data)
    anagrams(data)