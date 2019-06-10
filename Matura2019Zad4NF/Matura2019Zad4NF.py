from math import factorial
from math import gcd

def load_data(filename: str) -> list:
    with open(filename, "r") as file:
        return list(map(int, map(str.strip, file)))


def div_by_3(number: int) -> int:
    while number % 3 == 0:
        number /= 3
    return number


def power_of_3(data: list) -> int:
    return sum([1 for number in data if div_by_3(number) == 1])


def sum_of_fact(data: list) -> list:
    return [number for number in data if sum([factorial(int(fact)) for fact in str(number)]) == number]


def gcd_of_list(data: list, start: int, end: int) -> int:
    current_gcd = data[start]
    for i in range(start, end + 1):
        current_gcd = gcd(current_gcd, data[i])
    return current_gcd


def the_longest_NWD(data: list) -> list:
    data.insert(0, 1)
    data.append(1)
    max_len = 0
    start = 0
    end = 1
    current_gcd = gcd(data[0], data[1])
    while end < len(data):
        current_gcd = gcd(current_gcd, data[end])
        while current_gcd > 1 and end < len(data):
            if max_len < (end - start):
                max_gcd = current_gcd
                max_len = end - start
                starting = data[start]
            current_gcd = gcd(current_gcd, data[end])
            end += 1    
        while current_gcd == 1 and end < len(data) and start < end:
            start += 1
            current_gcd = gcd_of_list(data, start, end)
        if start == end and end < len(data):
            end += 1
    return [max_gcd, max_len, starting]


if __name__ == "__main__":
    data = load_data("liczby.txt")
    print(power_of_3(data))
    print(sum_of_fact(data))
    max_gcd, max_gcd_len, max_gcd_start = the_longest_NWD(data)
    print("GCD: ", max_gcd)
    print("Dlugosc: ", max_gcd_len)
    print("Poczatek: ", max_gcd_start)