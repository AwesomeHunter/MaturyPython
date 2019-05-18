import math

def isPalindrome(x):
    for i in range(math.floor(len(x)/2)):
        if x[i]!=x[len(x)-1-i]:
            return False
    return True

file = open("dane.txt", "r")

palindromes=0
maxOccurrence=None
moreThan1Occurr=0
numOfEven=0
occurrenceDict={}

for i in file:
    i=i.strip()
    occurrenceDict[i]=occurrenceDict.get(i, 0)+1
    if isPalindrome(i):
        palindromes+=1
    if occurrenceDict[i] == 2:
        moreThan1Occurr+=1
    if maxOccurrence == None:
        maxOccurrence=i
    if occurrenceDict[maxOccurrence]<occurrenceDict[i]:
        maxOccurrence=i
    if i[len(i)-1] == 'A' or i[len(i)-1] == 'C' or i[len(i)-1] == 'E':
        numOfEven+=1

file.close()

print("Liczba palindromow: "+str(palindromes))
print("Liczba liczb parzystych: "+str(numOfEven))
print("Najczesciej pojawiajacy sie wyraz: "+maxOccurrence+" - liczba wystapien: "+str(occurrenceDict[maxOccurrence]))
print("Liczba slow wystepujacych wiecej, niz raz: "+str(moreThan1Occurr))