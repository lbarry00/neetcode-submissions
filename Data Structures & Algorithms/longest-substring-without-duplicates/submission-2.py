class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        max_length = 0
        for r, c in enumerate(s):
            if c in seen:
                l = max(l, seen[c] + 1)
            seen[c] = r
            max_length = max(max_length, r - l + 1)
        
        return max_length