class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, n in enumerate(nums):
            # we won't find new result after this point because array is sorted
            if n > 0: break

            # skip already seen values
            if i > 0 and n == nums[i - 1]:
                continue
            
            target = 0 - n
            left = i + 1
            right = len(nums) - 1
            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum == target:
                    result.append([n, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # skip already seen values
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif two_sum < target:
                    left += 1
                elif two_sum > target:
                    right -= 1

        return result