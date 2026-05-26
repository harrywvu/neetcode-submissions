class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # brute force solution

        output = []
        exclude = 0
        val = 1
        for i in range(len(nums)):
            exclude = i
            for j in range(len(nums)):
                if j == exclude: continue
                val *= nums[j]
            output.append(val)
            val = 1
        return output