import random
# two sets of data vectors - is the input.
n = int(input("Size of dataset "))
pairXY = []

print("Input elements in pairs! ")
for x in range(n):
    a,b = (input().split(" "))
    pairXY.append((int(a), int(b)))


def sortUniformlyAtRandom(pairXY):
    pairXY.sort()
    a,b = "a","a"
    Arr = [[] for i in range(len(pairXY))]
    wasMultiple = False

    for i in range(len(pairXY)):
        na, nb = pairXY[i]
        if(na == a):
            if(wasMultiple == False):
                Arr[na].append(i-1)
            wasMultiple = True
        else:
            if(wasMultiple):
                Arr[a].append(i-1)
            wasMultiple = False     
        a,b = na, nb
    
    if(wasMultiple):
        Arr[a].append(len(pairXY) - 1)

    for i in range(len(Arr)):
        if(len(Arr[i])==0):
            continue
        else:
            start = i
            i += (Arr[i][1]-Arr[i][0]) 
            # shuffle start to i (both included)
            copy = pairXY[start:i+1]
            random.shuffle(copy)
            pairXY[start:i+1] = copy

sortUniformlyAtRandom(pairXY)
print(pairXY)

def Computation(pairXY, n):
    ranks = [0 for i in range(n)]
    ReverseRanks = [0 for i in range(n)]
    for a in range(n):
        for b in range(a+1):
            (xa, ya) = pairXY[a]
            (xb, yb) = pairXY[b]
            if(ya < yb):
                ranks[b]+=1
                ReverseRanks[a]+=1
            elif(ya > yb):
                ranks[a]+=1
                ReverseRanks[b]+=1
            elif((ya==yb) and (a!=b)):
                ranks[a]+=1
                ranks[b]+=1
                ReverseRanks[a]+=1
                ReverseRanks[b]+=1
    
    
    Numerator = 0
    Denominator = 0
    for x in range(n-1):
        Numerator+= (n* abs(ranks[x+1] - ranks[x]))
    for x in range(n):
        Denominator += 2*(ReverseRanks[x] * (n - ReverseRanks[x]))

    return (1 - (Numerator/Denominator))

answer = Computation(pairXY, n)
print("The Chatterjee Correlation Coefficient is " + str(answer))





            