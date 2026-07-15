class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        vowels = set(["a", "e", "i", "o", "u"])
        for i in range(len(queries)):
            count = 0
            ql, qr = queries[i][0], queries[i][1]
            for j in range(ql, qr + 1):
                word = words[j]
                if word[0] in vowels and word[-1] in vowels:
                    count += 1
            result.append(count)
        
        return result


