try:
    for j in range(1, 4):
        file=open("dane5-"+str(j)+".txt", "r")
        leaderDict={}
        leaderNum=None
        maxSum=None
        currentSum=0;
        for i in file:
            i=int(i);
            if(leaderNum==None):
                leaderNum=i
            if(maxSum==None):
                maxSum=i
            leaderDict[i]=leaderDict.get(i, 0)+1
            if(leaderDict[i]>leaderDict[leaderNum]):
                leaderNum=i
            currentSum+=i
            maxSum=max(maxSum, currentSum)
            if(currentSum<0):
                currentSum=0
        print("Plik "+str(j)+":")
        print("Maksymalna suma: "+str(maxSum))
        print("Element wystepujacy najczesciej: "+str(leaderNum))
        file.close()
except:
    print("Cos poszlo nie tak :c")