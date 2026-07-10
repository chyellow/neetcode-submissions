from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        grams = defaultdict(int)

        for char in s:
            grams[char] += 1
        
        for char in t:
            grams[char] -= 1
        
        for value in grams.values():
            if value != 0:
                return False
        
        return True