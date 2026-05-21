class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        visit = 0
        pointer = -1

        while visit < len(nums):
            pointer = (pointer+1)%len(nums)
            flag = True
            carry = None
            while flag:
                if nums[pointer] is None:
                    nums[pointer] = carry
                    # visit += 1
                    flag = False
                    # print(nums)
                    break
                
                tmp = carry
                carry = nums[pointer]
                nums[pointer] = tmp
                visit += 1

                # update reader and writer
                pointer = (pointer + k) % len(nums)
                # print(nums)
        