class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        open_brackets = ["(", "{", "["]
        close_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = deque()
        for c in s:
            if c in open_brackets:
                stack.append(c)
            elif len(stack) > 0:
                p = stack.pop()
                if close_map[c] != p:
                    return False
            else: 
                return False
        return len(stack) == 0