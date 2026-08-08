class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        max_length = 0
        l = 0

        for r in range(len(s)):
            c = s[r]
            l = max(l, last_index.get(c, 0))
            max_length = max(max_length, r - l + 1)
            last_index[c] = r + 1

        return max_length