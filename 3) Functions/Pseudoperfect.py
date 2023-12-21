from math import sqrt
n = int(input("Number: "))

d = []
for x in range(1, int(sqrt(n)+1)):
    if(n%x == 0):
        if(x!=n/x and x!=1):
            d.append(x)
            d.append(n//x)
        else:
            d.append(x)
print(d)
Len = len(d)
sums = [0 for i in range(1<<Len)]

for i in range(Len):
    L = (1<<i)
    sums[L] = d[i]

for x in range(1<<Len):
    if(sums[x]==0):
        for i in range(Len):
            if(x & (1<<i) == (1<<i)):
                sums[x]+=d[i]

# print(sums)
try:
    if(sums.index(n)):
        print("Yep, this is pseudoperfect!")

except ValueError:
    print("Nope, not pseudoperfect.")