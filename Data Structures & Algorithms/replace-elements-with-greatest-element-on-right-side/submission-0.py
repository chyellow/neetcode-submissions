class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currMax = -1

        for r in range((len(arr) - 1), - 1, -1):
            newMax = max(currMax, arr[r])
            arr[r] = currMax
            currMax = newMax
        
        return arr
            