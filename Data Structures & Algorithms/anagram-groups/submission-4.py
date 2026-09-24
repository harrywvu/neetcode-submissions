class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            ss = ''.join(sorted(s))

            anagrams[ss].append(s)
        
        return list(anagrams.values())