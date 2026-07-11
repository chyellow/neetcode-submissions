from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a_map = defaultdict(int)

        for char in s:
            a_map[char] += 1
        
        for char in t:
            a_map[char] -= 1
            
        for key in a_map.values():
            if key != 0:
                return False
        
        return True
                