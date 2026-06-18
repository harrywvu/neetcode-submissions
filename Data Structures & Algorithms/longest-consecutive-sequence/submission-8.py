class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums: return 0

        # remove duplicates and sort
        s_nums = sorted(set(nums))

        # [1, 2, 3, 10, 11, 15, 17]
        
        # find the starting sequence
        starters = []
        for n in s_nums:
            if n - 1 not in s_nums: starters.append(n)

        # current = s_nums[0]
        longest = 0

        # # confirm current is a starting sequence
        # while current - 1 not in s_nums:
            
            
        #     # idk how to properly go to the next one
        #     current = 
        
        # return longest

        for n in starters:
            current = n
            length = 1

            while current + 1 in s_nums:
                current += 1
                length += 1

            longest = max (longest, length)

        return longest
