def Solve(X, n, i):
    elt = X[i]
    for j in range(min(i+1, n-i)):
        if X[i+j] > elt:
            return X[i+j]
        elif X[i-j] > elt:
            return X[i-j]
    
    index = min(i + 1, n - i)
    if index == i+1:
        for j in range(2*i+1, n):
            if X[j] > elt:
                return X[j]
    else:
        for j in range(2*i - n, -1, -1):
            if X[j] > elt:
                return X[j]

X = [1,4,3,2,5,7]
print(Solve(X, 6, 4))