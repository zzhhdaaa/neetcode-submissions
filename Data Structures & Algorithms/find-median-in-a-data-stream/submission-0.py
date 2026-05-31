class MedianFinder:

    def __init__(self):
        # we use a max heap at the left, and min heap at the right
        self.left = [] # this is a max heap
        self.right = [] # this is a min heap
        self.count = 0 # this is the total num

    def rebalance(self) -> None:
        # we always want to keep the left count == right count or right count +1
        if len(self.left) == len(self.right) or len(self.left) == len(self.right)+1:
            return
        
        elif len(self.left) > len(self.right)+1:
            num = heapq.heappop_max(self.left)
            heapq.heappush(self.right, num)
        elif len(self.left) < len(self.right):
            num = heapq.heappop(self.right)
            heapq.heappush_max(self.left, num)
        

    def addNum(self, num: int) -> None:
        if len(self.right) == 0 or num <= self.right[0]:
            heapq.heappush_max(self.left, num)
        else:
            heapq.heappush(self.right, num)
        self.count += 1
        self.rebalance()
        

    def findMedian(self) -> float:
        if self.count%2 == 1:
            return self.left[0]
        return (self.left[0]+self.right[0])*0.5
        
        