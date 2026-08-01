class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in anagramMap:
                anagramMap[sorted_s].append(s)
            else:
                anagramMap[sorted_s] = [s]
            
        
        return list(anagramMap.values())