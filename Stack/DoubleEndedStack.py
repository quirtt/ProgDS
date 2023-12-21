class deque():
    def __init__(self, size):
        self.size = size
        self.deque = [None]*size
        self.top1 = -1
        self.top2 = size
    
    def push1(self, item):
        if self.top1 < self.top2 - 1:
            self.top1+=1
            self.deque[self.top1] = item
        else:
            raise IndexError('Overflow: Insufficient space.')
    
    def pop1(self):
        if self.top1 > -1:
            self.top1 -= 1
            return self.deque[self.top1 + 1]
        else:
            raise IndexError('Underflow: Negative space inaccessible.')
    

    def push2(self, item):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.deque[self.top2] = item
        else:
            raise IndexError('Overflow: Insufficient space.')
    
    def pop2(self):
        if self.top2 < self.size:
            self.top2 += 1
            return self.deque[self.top - 1]
        else:
            raise IndexError('Underflow: Negative space inaccessible.')
    
X = deque(2)
X.push1(10)
X.push2(20)
# X.push1(15)
# X.push2(15)
print(X.deque)