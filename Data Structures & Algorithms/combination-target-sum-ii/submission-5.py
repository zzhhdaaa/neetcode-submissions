class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # dfs: take or not
        # node
        # 9, []
        # node, node
        # 2, [], 2, []
        # node, node, node, node
        # 2, [], 2, [], 2, [], 2, []
        # [9,2,2] [9,2] [9,2] [9] [2,2] [2] [2] []
        # return when running out of node, or sum to the target
        #
        # find a way to remove the duplicates
        candidates = sorted(candidates)
        results = set()
        curr = []

        def dfs(i: int):
            if sum(curr) == target:
                results.add(tuple(curr.copy()))
                return
            if i >= len(candidates):
                return
            
            curr.append(candidates[i])
            dfs(i+1)

            curr.pop()
            dfs(i+1)
        
        dfs(0)

        return [list(result) for result in results]
