class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []

        result = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:  
                c_index = ord(c) - ord('a')
                freq[c_index] += 1
            result[tuple(freq)].append(s)

        return list(result.values())
