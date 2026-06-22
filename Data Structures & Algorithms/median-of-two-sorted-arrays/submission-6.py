import bisect

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = nums2, nums1
        
        l, r = 0, len(A)-1
        while True:
            m1 = (l + r) // 2   # A
            m2 = half - m1 - 2  # B

            Aleft = A[m1] if 0<=m1<len(A) else float('-inf')
            Aright = A[m1+1] if 0<=m1+1<len(A) else float('inf')
            Bleft = B[m2] if 0<=m2<len(B) else float('-inf')
            Bright = B[m2+1] if 0<=m2+1<len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total%2 == 1:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = m1 - 1
            else:
                l = m1 + 1