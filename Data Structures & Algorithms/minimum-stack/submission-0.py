class MinStack:

    def __init__(self):
        self.mainstack = []
        self.auxstack = []
        

    def push(self, val: int) -> None:
        self.mainstack.append(val)
        if len(self.auxstack) == 0 or val <= self.auxstack[-1]:
            self.auxstack.append(val)

    def pop(self) -> None:
        topvalue = self.mainstack.pop()
        if topvalue == self.auxstack[-1]:
            self.auxstack.pop()
        
        

    def top(self) -> int:
        return self.mainstack[-1]
        

    def getMin(self) -> int:
        return self.auxstack[-1]
        
