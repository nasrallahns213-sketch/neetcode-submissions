class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        def two_sum(nums, target):
            numbers = {}
            for i, num in enumerate(nums):
                complement = target - num
                if complement in numbers:
                    j = numbers[complement]
                    return [j, i] if j < i else [i, j]
                numbers[num] = i
            return None
        return two_sum(nums, target)