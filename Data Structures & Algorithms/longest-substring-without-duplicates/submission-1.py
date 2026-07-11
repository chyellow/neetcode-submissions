class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        result = 0
        char_map = set()

        for r in range(len(s)):
            while s[r] in char_map:
                char_map.remove(s[l])
                l += 1
            char_map.add(s[r])
            result = max(result, r - l + 1)
        
        return result