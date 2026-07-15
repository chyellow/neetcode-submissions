class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        result = 0

        for r in range(len(nums)):
            if nums[r] == 1:
                result = max(result, r - l + 1)
            else:
                l = r + 1

        return result