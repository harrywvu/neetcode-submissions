class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
    # the solution must track the characters that exist in s, and have their duplicates accordingly.
    # t must have the same characters and same amount of those characters in order to be true
    # coming up with a solution is hard tbh

    # first suggested solution: i use a dictionary to keep track of all s and t characters by using a 'character : frequency' pairing.
    # afterwards, we check each pair in both dictionaries to see if they match.

        sDict = {}
        tDict = {}

        for x in s:
            sDict[x] = sDict.get(x, 0) + 1
        for x in t:
            tDict[x] = tDict.get(x, 0) + 1

        return True if sDict == tDict else False