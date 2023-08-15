#assignisik@gmail.com
def is_special(n):
    digits = []
    tmp = n
    while(n > 0):
        dig = n%10
        n//=10
        digits.append(dig)
    prod_dig = 1
    sum_dig = 0
    for dig in digits:
        prod_dig*=dig
        sum_dig+=dig

    return tmp == (prod_dig + sum_dig)

def checkSpecial(m):
    nArray = []
    # num of digits is n
    for x in range(10**(m-1), 10**(m)):
        if(is_special(x)):
            nArray.append(x)
    
    return nArray
m = int(input("Check whether special: "))
print(is_special(m))
n = int(input("Number of digits? "))
print(checkSpecial(n))
