vowels = ['a', 'e', 'i', 'o', 'u']

def checkNICE(Str):
    vowelArray = []
    for i in range(len(Str)):
        if(Str[i] in vowels):
            vowelArray.append(i)
    
    # Check if vowelArray is an AP
    if(len(vowelArray) <= 1):
        return True
    else:
        start = vowelArray[0]
        second = vowelArray[1]
    for i in range(len(vowelArray) - 1):
        if(vowelArray[i+1] - vowelArray[i] != second-start):
            return False
    
    return True

Str = input("String?: ")
print(checkNICE(Str))