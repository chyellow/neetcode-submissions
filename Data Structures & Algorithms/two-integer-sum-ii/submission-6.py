class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        track = {}
        
        for i, num in enumerate(numbers):
            difference = target - num
            if difference in track:
                return [track[difference] + 1, i + 1]
            track[num] = i
        
        return []