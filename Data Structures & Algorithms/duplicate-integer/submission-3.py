class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:

        # go through the entire array and compare each element to another, until we find the first match to which we will immediately return true.
        # But, this is obviously the worst possible solution, since it wouldn't be any form of ideal if the list scales.
        # A set is perfect for this scenario, however, I have no clue how to implement it. Do I convert the list of integers into an list? How do I do that?
        # my second suggested solution, do a conditional if a list can be converted into a set:
        # if set(nums):
        #     return False
        # else: return True
        # so wrong lol. apparently, this just checks if the set is empty.

        # my third suggested solution, create a set with the elements of the list. if the set adds a duplicate, it returns true, otherwise, false
        s = set()
        for x in nums:
            if x not in s: s.add(x)
            elif x in s: return True
        
        return False