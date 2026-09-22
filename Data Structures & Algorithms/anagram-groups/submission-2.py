class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]

        anagrams = defaultdict(list)

        for s in strs:

            ss = ''.join(sorted(s))

            anagrams[ss].append(s)

        return list(anagrams.values())