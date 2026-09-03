class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        target = len(count1)

        for i in range(len(s2)):
            count2 = {}
            subtr_len = 0
            
            for j in range(i, len(s2)):
                n = s2[j]
                count2[n] = 1 + count2.get(n, 0)

                if count1.get(n, 0) < count2.get(n, 0):
                    break
                if count2.get(n, 0) == count1.get(n, 0):
                    subtr_len += 1
                if target == subtr_len:
                    return True
            
        return False