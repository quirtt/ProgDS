def infix_to_postfix(X):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []

    for char in X.split():
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence.get(char, 0) <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ' '.join(output)

X = input("")
output = infix_to_postfix(X)
print(output)
