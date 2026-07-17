class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in complements:
                # if matching val was found previously
                return [complements[complement], i]
            else:
                # [value, index]
                complements[nums[i]] = i
        return []