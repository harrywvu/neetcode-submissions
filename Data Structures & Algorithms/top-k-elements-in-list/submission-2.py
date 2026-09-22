class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []

        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        return sorted(freq, key=lambda x: freq[x], reverse=True)[:k]