class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        self.minHeap.append(val)
        index = len(self.minHeap) - 1
        parentIndex = self.getParent(index)
        
        while index > 0 and self.minHeap[parentIndex] > self.minHeap[index]:
            self.minHeap[parentIndex], self.minHeap[index] = self.minHeap[index], self.minHeap[parentIndex]
            index = parentIndex
            parentIndex = self.getParent(index)
        
        if len(self.minHeap) > self.k:
            self.minHeap[0], self.minHeap[len(self.minHeap)-1] = self.minHeap[len(self.minHeap)-1], self.minHeap[0]
            self.minHeap.pop()
            index = 0
            leftChild = self.getLeftChild(index)
            rightChild = self.getRightChild(index)

            while (leftChild < len(self.minHeap) and self.minHeap[leftChild] < self.minHeap[index]) or \
                (rightChild < len(self.minHeap) and self.minHeap[rightChild] < self.minHeap[index]):
                if rightChild >= len(self.minHeap) or \
                    (leftChild < len(self.minHeap) and self.minHeap[leftChild] < self.minHeap[rightChild]):
                    self.minHeap[leftChild], self.minHeap[index] = self.minHeap[index], self.minHeap[leftChild]
                    index = leftChild
                elif leftChild >= len(self.minHeap) or \
                    (rightChild < len(self.minHeap) and self.minHeap[leftChild] >= self.minHeap[rightChild]):
                    self.minHeap[rightChild], self.minHeap[index] = self.minHeap[index], self.minHeap[rightChild]
                    index = rightChild
                leftChild = self.getLeftChild(index)
                rightChild = self.getRightChild(index)
        
        return self.minHeap[0]

    
    def getParent(self, index: int) -> int:
        return (index-1) // 2
    
    def getLeftChild(self, index: int) -> int:
        return index * 2 + 1
    
    def getRightChild(self, index: int) -> int:
        return index * 2 + 2
