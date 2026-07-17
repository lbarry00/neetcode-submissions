class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        numsAsSet = set(nums)
        longestSequenceLength = 0

        for i in range(len(nums)):
            val = nums[i]
            if (val-1) not in numsAsSet:
                # this is the start of a sequence
                seqLength = 0
                itr = 0
                while (True):
                    # seek forward for sequence values until
                    # we run out of matching values
                    if (val + itr) in numsAsSet:
                        seqLength += 1
                        itr += 1
                    else:
                        break
                
                longestSequenceLength = max(longestSequenceLength, seqLength)

        return longestSequenceLength