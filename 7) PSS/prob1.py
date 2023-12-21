# Given a list of non-negative digits (0-9), not necessarily
# distinct, write a program to find out the largest multiple of 3
# that can be formed from these digits. E.g., if the sample input
# is 19234493219, the output will be 9994433211.
def function(x):
    freq = [0]*10
    sum = 0
    for c in x:
        freq[ord(c) - ord('0')]+=1
        sum += ord(c) - ord('0')

    Stack = []
    i = 0
    Mod = sum % 3
    isDone = False or (Mod == 0)
    if not isDone:
        NegCtr = 0
        val1, val2 = 20, 20
        for i in range(10):
            if freq[i]:
                if i%3 == Mod:
                    isDone = True
                    freq[i]-=1
                if i%3 == 3 - Mod:
                    NegCtr += freq[i]
                    val1 = min(val1, i)
                    val2 = min(i, val2) if (val1 != i) or (freq[i] >= 2) else val2
                

        if not isDone: 
            if NegCtr >= 2:
                freq[val1]-=1
                freq[val2]-=1
                isDone = True

    for i in range(10):
        while(freq[i]):
            Stack.append(i)
            freq[i]-=1

    
    answer = ''
    if isDone: 
        while Stack:
            answer += str(Stack.pop())
    
    if answer:
        answer = int(answer)
    
    return answer


x = str(input("integer?: "))
print(function(x))