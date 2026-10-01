class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct_nums = set()

        for n in nums:  
            if n in distinct_nums: 
                return True
            else: distinct_nums.add(n)
        
        return False