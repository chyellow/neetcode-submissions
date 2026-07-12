class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        seen = set(nums)

        for num in nums:
            length = 0
            if num - 1 not in seen:
                length = 0
                while(num + length in seen):
                    length += 1
                result = max(length, result)
        
        return result