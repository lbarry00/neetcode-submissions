class Solution:
    def topKFrequent(self, nums: List[int], k: int)  -> List[int]:
        # <value, frequency>
        freq_map = {}
        freq_vals = [[] for i in range(len(nums) + 1)]

        for n in nums:
            freq_map[n] = 1 + freq_map.get(n, 0)
        for n, f in freq_map.items():
            freq_vals[f].append(n)

        result = []
        for i in range((len(freq_vals) - 1), 0, -1):
            for n in freq_vals[i]:
                result.append(n)
                if len(result) == k:
                    return result