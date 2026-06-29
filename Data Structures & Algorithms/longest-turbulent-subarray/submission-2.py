class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        count = 1
        prev = arr[0]
        flag = 0 # 0 -> equal, 1 -> greater, 2 -> smaller

        for i in range(len(arr)):
            if flag == 0:
                if arr[i] == prev:
                    continue
                else:
                    count += 1
            elif flag == 1:
                if arr[i] < prev:
                    count += 1
                else:
                    count = 1 if arr[i] == prev else 2
            elif flag == 2:
                if arr[i] > prev:
                    count += 1
                else:
                    count = 1 if arr[i] == prev else 2
            
            flag = 0 if arr[i] == prev else 1 if arr[i] > prev else 2
            prev = arr[i]
            res = max(res, count)
        
        return res

