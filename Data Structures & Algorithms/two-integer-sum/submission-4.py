class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in sum_map:
                return [sum_map[difference], i]
            sum_map[num] = i
        return