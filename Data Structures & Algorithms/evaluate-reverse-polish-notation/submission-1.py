class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]

        s = deque()
        for n in tokens:
            if n not in operators:
                s.append(int(n))
                continue
            
            b = s.pop()
            a = s.pop()
            
            if n == "+":
                s.append(a + b)
            elif n == "-":
                s.append(a - b)
            elif n == "*":
                s.append(a * b)
            else:
                s.append(int(a / b))

        return s.pop()