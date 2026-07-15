class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []

        for curr_word in words:
            for word in words:
                if curr_word != word and curr_word in word:
                    result.append(curr_word)
                    break

        return result