class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l, r = 0, mountainArr.length()-1

        low = min(mountainArr.get(l), mountainArr.get(r))
        if target < low:
            return -1
        peak = -1

        while l < r:
            m = (l+r) // 2

            mleft = mountainArr.get(m-1)
            mval = mountainArr.get(m)
            mright = mountainArr.get(m+1)

            if mleft < mval and mright < mval:
                peak = m
                if target > mval:
                    return -1
                break
            elif mval < mright:
                l = m + 1
            elif mval < mleft:
                r = m
        
        # 1,2,3,4,2,1
        l, r = 0, peak

        while l < r:
            m = (l+r) // 2
            mval = mountainArr.get(m)

            if mval == target:
                return m
            elif mval < target:
                l = m + 1
            elif mval > target:
                r = m
        
        l, r = peak, mountainArr.length()

        while l < r:
            m = (l+r) // 2
            mval = mountainArr.get(m)

            if mval == target:
                return m
            elif mval < target:
                r = m
            elif mval > target:
                l = m + 1
        
        return -1