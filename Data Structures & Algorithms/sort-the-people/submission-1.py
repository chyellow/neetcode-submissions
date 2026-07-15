class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height = {}
        result = []
        for i in range(len(names)):
            height[heights[i]] = names[i]
        
        for h in reversed(sorted(height)):
            result.append(height[h])
        
        return result