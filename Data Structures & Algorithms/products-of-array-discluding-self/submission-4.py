class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        suf = [0] * len(nums)
        p_mul = s_mul = 1

        for i in range (len(nums)):
            j = -i -1

            pre[i] = p_mul
            suf[j] = s_mul
            p_mul *= nums[i]
            s_mul *= nums[j]
        
        return [p*s for p,s in zip(pre,suf)]