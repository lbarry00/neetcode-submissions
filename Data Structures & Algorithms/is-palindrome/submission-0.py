class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0: return False

        # remove non-alphanumeric, convert to lower case
        sanitized = "".join(filter(str.isalnum, s))
        sanitized = sanitized.lower()
        l = 0
        r = len(sanitized) - 1
        while (l < r):
            if sanitized[l] != sanitized[r]:
                return False
            else:
                l += 1
                r -= 1

        return True