class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""

        tCount = {}
        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)

        have, need = 0, len(tCount)
        window = {}
        result, substr_len = "", float("infinity")
        l = 0
        
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in tCount and window[s[r]] == tCount[s[r]]:
                have += 1

            while have == need: 
                if (r - l + 1) < substr_len:
                    substr_len = r - l + 1
                    result = s[l:r + 1]
                window[s[l]] -= 1
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1

        return result
