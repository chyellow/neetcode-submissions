class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        seen = set()

        for i in range(len(words)):
            currWord = words[i]
            for word in words:
                if len(currWord) >= len(word):
                    continue
                l = 0
                r = len(currWord) - 1
                while r < len(word):
                    if word[l:r + 1] == currWord:
                        if currWord not in seen:
                            result.append(currWord)
                            seen.add(currWord)
                        break
                    l += 1
                    r += 1
        return result

