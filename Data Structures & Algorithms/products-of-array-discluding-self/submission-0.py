class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_prods = [1]
        l_prod = 1
        for i in range(len(nums)-1):
            l_prod *= nums[i]
            l_prods.append(l_prod)
        
        r_prods = [1]
        r_prod = 1
        for i in range(len(nums)-1, 0, -1):
            r_prod *= nums[i]
            r_prods.append(r_prod)
        r_prods.reverse()

        prods = []
        for i in range(len(nums)):
            prod = l_prods[i] * r_prods[i]
            prods.append(prod)
        
        return prods

        