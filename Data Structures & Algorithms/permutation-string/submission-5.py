class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = defaultdict(int)
        window = defaultdict(int)

        # Count s1
        for char in s1:
            need[char] += 1

        # Count first window in s2
        window_size = len(s1)

        for i in range(window_size):
            window[s2[i]] += 1

        if window == need:
            return True

        # Slide the window
        for right in range(window_size, len(s2)):
            left = right - window_size

            # Add new right character
            window[s2[right]] += 1

            # Remove old left character
            window[s2[left]] -= 1

            # Important: delete keys that reach 0
            if window[s2[left]] == 0:
                del window[s2[left]]

            if window == need:
                return True

        return False