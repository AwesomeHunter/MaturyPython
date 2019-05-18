import math as m   

def sumOfDigits(x):
    sum=0
    while x!=0:
        sum+=x%10
        x=m.floor(x/10)
    return sum

def binarySum(x):
    sum=0
    while x>0:
        sum+=x%2
        x=m.floor(x/2)
    return sum

def countBPrimes(x, y, primesTab):
    print("Liczby super B pierwsze w przedziale "+str(x)+" - "+str(y)+":")
    sum=0
    for i in range(x, y+1):
        if primesTab[i]==False and primesTab[sumOfDigits(i)]==False and primesTab[binarySum(i)]==False:
            sum+=1
            #print(i) - Zapisanie do pliku/wyswietlenie
    print("Ilosc liczb super B pierwszych w tym przedziale: "+str(sum))
    return

def countSumOfDigitsPrimes(x, y, primesTab):
    sum=0
    for i in range(x, y+1):
        if primesTab[sumOfDigits(i)]==False:
            sum+=1
    print("Ilosc liczb w przedziale "+str(x)+" - "+str(y)+", ktorych suma cyfr jest liczba pierwsza: "+str(sum)) 
    return

def countSumBPrimes(x, y, primesTab):
    sum=0
    for i in range(x, y+1):
        if primesTab[i]==False and primesTab[sumOfDigits(i)]==False and primesTab[binarySum(i)]==False:
            sum+=i
    j=2
    while j*j<=sum:
        if sum%j==0:
            print("Suma liczb super B pierwszych w przedziale "+str(x)+" - "+str(y)+" nie jest liczba pierwsza")
            return
        j+=1
    print("Suma liczb super B pierwszych w przedziale "+str(x)+" - "+str(y)+" jest liczba pierwsza")
    return
      
#----------------------------------------------

primes = [False]*100001
primes[0]=True
primes[1]=True
for i in range(2, 320):
    if primes[i]==False:
        j=i*i
        while j<100001:
            primes[j]=True
            j+=i

countBPrimes(2, 1000, primes)
countBPrimes(100, 10000, primes)
countBPrimes(1000, 100000, primes)
countSumOfDigitsPrimes(100,10000, primes)
countSumBPrimes(100, 100000, primes)