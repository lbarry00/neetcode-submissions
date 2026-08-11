class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        product = None
        zero_count = 0
        for n in nums:
            if n == 0:
                zero_count += 1
            elif product == None:
                product = n
            else:
                product *= n
        
        if product == None: product = 0

        for n in nums:
            if zero_count > 1:
                result.append(0)
            elif zero_count == 1 and n != 0:
                result.append(0)
            elif n == 0:
                result.append(product)
            else:
                result.append(int(product / n))

        return result