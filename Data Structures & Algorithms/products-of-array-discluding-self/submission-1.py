class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        p_mul = s_mul = 1

        # populate the prefix products 
        for i in range (len(nums)):
            j = -i -1
            prefix[i] = p_mul
            suffix[j] = s_mul
            p_mul *= nums[i]
            s_mul *= nums[j]

        return [p*s for p,s in zip(prefix, suffix)]