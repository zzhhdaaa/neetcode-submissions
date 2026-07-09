class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.values = [-1] * k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.values[self.rear] = value
        self.rear = self.rear + 1 if self.rear < self.k - 1 else 0
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.values[self.front] = -1
        self.front = self.front + 1 if self.front < self.k - 1 else 0
        return True

    def Front(self) -> int:
        return self.values[self.front]

    def Rear(self) -> int:
        rear = self.rear - 1 if self.rear > 0 else self.k - 1
        return self.values[rear]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.values[self.front] == -1

    def isFull(self) -> bool:
        if self.k == 1:
            return self.values[0] != -1
        return self.front == self.rear and self.values[self.rear] != -1


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()