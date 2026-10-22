class MinStack:

    def __init__(self):
        self.stack =[]
        self.minStack =[]

    def push(self, val: int) -> None:
        self.stack.append(val)


        if self.minStack: # if non empty minStack
            val = min(val, self.minStack[-1]) # val compares val with top of minStack
        else:
            val = val
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:    
        return self.minStack[-1]








        # tmp = []
        # minVal = self.stack[-1]
        # while len(self.stack):
        #     minVal = min(minVal, self.stack[-1])
        #     tmp.append(self.stack.pop())

        # while len(tmp):
        #     self.stack.append(tmp.pop())

        # return minVal


        


        

        
