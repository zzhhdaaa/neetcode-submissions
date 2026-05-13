class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = [0] * 41 # every int's count from -20 to 20. idx 0 -> num -20
        visit = set()

        def dfs(i: int, prev: list):
            if i >= len(nums):
                key = "".join(str(count))
                if not key in visit:
                    res.append(prev.copy())
                    visit.add(key)
                return
            
            prev.append(nums[i])
            count[nums[i]+20] += 1
            dfs(i+1, prev)

            prev.pop()
            count[nums[i]+20] -= 1
            dfs(i+1, prev)

        dfs(0, [])
        return list(res)