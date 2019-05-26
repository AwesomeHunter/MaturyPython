div2 = 0
div8 = 0
more_0_than_1 = 0
biggest = None
biggest_index = None
smallest = None
smallest_index = None

with open("liczby.txt") as file:
    for index, line in enumerate(file, 1):
        line = line.strip()
        if line.count("0") > line.count("1"):
            more_0_than_1 += 1
        line = line.lstrip("0")
        if line[-1] != "1":
            div2 += 1
        if len(line) > 3 and "1" not in line[-3:]:
            div8 += 1
        if (biggest is None) or (len(line) > len(biggest)):
            biggest = line
            biggest_index = index
        elif len(biggest) == len(line):
            for i in range(len(biggest)):
                if line[i] == "1" and biggest[i] == "0":
                    biggest = line
                    biggest_index = index
                    break
                elif line[i] == "0" and biggest[i] == "1":
                    break
        if (smallest is None) or (len(line) < len(smallest)):
            smallest = line
            smallest_index = index
        elif len(smallest) == len(line):
            for i in range(len(smallest)):
                if line[i] == "0" and smallest[i] == "1":
                    smallest = line
                    smallest_index = index
                    break
                elif line[i] == "1" and smallest[i] == "0":
                    break
print("Ilosc liczb podzielnych przez 2:", div2)
print("Ilosc liczb podzielnych przez 8:", div8)
print("Ilosc liczb z wieksza iloscia 0 niz 1:", more_0_than_1)
print("Najwieksza liczba:", biggest_index)
print("Najmniejsza liczba:", smallest_index)