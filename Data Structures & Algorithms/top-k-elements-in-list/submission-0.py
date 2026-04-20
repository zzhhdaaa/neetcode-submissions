class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums)+1)]
        for num, cnt in freq.items():
            buckets[cnt].append(num)
        
        topNums = []
        for i in range(len(nums), -1, -1):
            for num in buckets[i]:
                topNums.append(num)
                if len(topNums) >= k:
                    return topNums