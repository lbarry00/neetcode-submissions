class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        for i, n in enumerate(nums):
            if i == 0:
                prefix[i] = n
            else: 
                prefix[i] = prefix[i - 1] * n

        postfix = [0] * len(nums)
        for i, n in reversed(list(enumerate(nums))):
            if i == len(nums) - 1:
                postfix[i] = n
            else: 
                postfix[i] = postfix[i + 1] * n
        
        result = [0] * len(nums)
        for i, n in enumerate(nums):
            left = prefix[i - 1] if i > 0 else 1
            right = postfix[i + 1] if i < len(nums) - 1 else 1
            result[i] = left * right

        return result