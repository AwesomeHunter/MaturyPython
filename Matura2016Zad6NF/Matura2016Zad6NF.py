import string

with open("dane_6_1.txt", "r") as file:
    letters = string.ascii_uppercase[107%26:] + string.ascii_uppercase[:107%26]
    letters_tab = str.maketrans(string.ascii_uppercase, letters)
    with open("wyniki_6_1.txt", "w+") as answer_file:
        for line in file:
            answer_file.write(line.translate(letters_tab))
            
with open("dane_6_2.txt", "r") as file:
    with open("wyniki_6_2.txt", "w+") as answer_file:
        for line in file:
            line = line.strip()
            line_words = line.split()
            if len(line_words) == 2:
                letters = string.ascii_uppercase[int(line_words[1])%26:] + string.ascii_uppercase[:int(line_words[1])%26]
                letters_tab = str.maketrans(letters, string.ascii_uppercase)
                answer_file.write(line.translate(letters_tab)+'\n')
            else:
                answer_file.write(line+'\n')
                
with open("dane_6_3.txt", "r") as file:
    with open("wyniki_6_3.txt", "w+") as answer_file:
        for line in file:
            line = line.strip()
            line_words = line.split()
            if len(line_words) == 2:
                for i in range(len(line_words[1])-1):
                    if (ord(line_words[0][i])-ord(line_words[1][i])+26)%26 != (ord(line_words[0][i+1])-ord(line_words[1][i+1])+26)%26:
                        answer_file.write(line_words[0]+'\n')
                        break
            else:
                answer_file.write(line+'\n')