class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = [[] for i in range(len(nums) + 1)]

        for n in nums:
            if n not in freq: freq[n] = 1
            else: freq[n] += 1

        for key, val in freq.items():
            count[val].append(key)

        res = []
        for i in range(len(count) -1, 0, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res