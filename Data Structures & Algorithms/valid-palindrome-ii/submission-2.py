class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                stepL, stepR = s[l + 1: r +  1], s[l:r]
                return stepL == stepL[::-1] or stepR == stepR[::-1]
            l += 1
            r -= 1
        return True