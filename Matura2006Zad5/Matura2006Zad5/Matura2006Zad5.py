import sys

dayTab=["poniedzialek", "wtorek", "sroda", "czwartek", "piatek", "sobota", "niedziela"]
dayDict={"poniedzialek":0, "wtorek":1, "sroda":2, "czwartek":3, "piatek":4, "sobota":5, "niedziela":6}

try:
    day = input("podaj dz. tygodnia: ")
    day=day.lower()
    year = input("podaj rok: ")
    year=int(year)
except:
    print("Bledne dane!")
    sys.exit()

if day not in dayTab or year<1500 or year>2005:
    print("Bledne dane!")
    sys.exit()

currentYear=1582

print()
print("Odp:")

if(year>1582):
    days=109
    currentYear+=1
    while(currentYear<year):
        days+=365
        if(currentYear%4==0 and (currentYear%100!=0 or currentYear%400==0)):
            days+=1
        currentYear+=1
    currentDay=1+(dayDict[day]-dayDict[dayTab[(4+days)%7]]+7)%7
    while(currentDay<=28):
        print(str(currentDay)+".02."+str(year))
        currentDay+=7
    if(currentYear%4==0 and (currentYear%100!=0 or currentYear%400==0) and currentDay==29):
        print(str(currentDay)+".02."+str(year))
else:
    days=245
    while(currentYear>year):
        days+=365
        currentYear-=1
        if(currentYear%4==0):
            days+=1
    currentDay=1+(dayDict[day]-dayDict[dayTab[(3-days+7000000)%7]]+7)%7
    while(currentDay<=28):
        print(str(currentDay)+".02."+str(year))
        currentDay+=7
    if(currentYear%4==0 and currentDay==29):
        print(str(currentDay)+".02."+str(year))