class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        index1 = 0
        index2 = 0

        while (left <= right):
            two_sum = numbers[left] + numbers[right]
            if two_sum == target:
                index1 = left + 1
                index2 = right + 1
                break
            elif two_sum < target:
                left += 1
            else:
                right -= 1

        return [index1, index2]