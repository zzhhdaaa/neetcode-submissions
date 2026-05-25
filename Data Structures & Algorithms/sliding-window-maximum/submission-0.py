class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = defaultdict(int)

        for i in range(k-1):
            window[nums[i]] += 1
        
        res = []
        for i in range(0, len(nums)-k+1):
            left = i
            right = i+k-1

            window[nums[right]] += 1
            largest = max(window.keys())
            res.append(largest)

            window[nums[left]] -= 1
            if window[nums[left]] == 0:
                window.pop(nums[left])
        
        return res