class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        key = tuple(sorted(s1))
        
        l = 0
        r = len(s1) - 1
        
        while r < len(s2):
            s2_key = tuple(sorted(s2[l:r + 1]))
            if s2_key == key:
                return True
            else:
                l += 1
                r += 1
        return False
