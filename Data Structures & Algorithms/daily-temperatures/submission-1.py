class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        s = []

        for i, n in enumerate(temperatures):
            while s and n > temperatures[s[-1]]:
                idx = s.pop()
                result[idx] = i - idx
            s.append(i)
            
        return result