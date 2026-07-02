class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        xflag = False
        yflag = False
        zflag = False

        for a, b, c in triplets:
            if a>x or b>y or c>z:
                continue
            xflag = xflag or a==x
            yflag = yflag or b==y
            zflag = zflag or c==z
        
        return xflag and yflag and zflag