class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]
        count = 0

        for i in range(1, len(f) - 1):
            l = i - 1
            r = i + 1
            if f[i] == 0:
                if f[l] == 0 and f[r] == 0:
                    count += 1
                    f[i] = 1
        return n <= count

