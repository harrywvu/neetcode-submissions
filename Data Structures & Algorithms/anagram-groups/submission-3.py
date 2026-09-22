class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        anagrams = defaultdict(list) # preinitialize the dict with lists dynamically

        for s in strs:

            ss = ''.join(sorted(s)) # sorted sorts the string but returns it as a list of chars. join is used to turn it into a string

            anagrams[ss].append(s) # use ss as a unique identifier for all anagrams and append them to their list

        return list(anagrams.values())
        # idk why [anagrams.values()] doesnt work