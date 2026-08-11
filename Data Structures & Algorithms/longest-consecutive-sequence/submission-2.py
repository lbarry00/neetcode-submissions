class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        nums_as_set = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in nums_as_set:
                # this is the start of a sequence
                target = n + 1

                # seek forward for sequence values until
                # we run out of matching values
                while target in nums_as_set:
                    # remove current val so don't have to 
                    # check again in the future
                    nums_as_set.remove(target)
                    target += 1
                    
                longest = max(longest, target - n)

        return longest