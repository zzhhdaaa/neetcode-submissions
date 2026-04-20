class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.main_stack.append(val)

        if len(self.min_stack) == 0 or val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.main_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if len(self.main_stack) != 0:
            return self.main_stack[-1]

    def getMin(self) -> int:
        if len(self.min_stack) != 0:
            return self.min_stack[-1]
        
