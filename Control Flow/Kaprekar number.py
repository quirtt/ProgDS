def is_Kaprekar(n):
    n_str = str(n)
    digs = len(n_str)
    val = n**2
    val_str = str(val)
    nRight = val_str[-1:-1-digs:-1][-1::-1]
    nLeft = val_str[0:digs]
    nMinus1 = val_str[0:digs-1]
    return (int(nRight)+int(nLeft) == n or int(nRight)+int(nMinus1) == n)

n = int(input("Number?: "))
print(is_Kaprekar(n))