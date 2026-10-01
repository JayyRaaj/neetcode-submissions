class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        char_set = set(s)  # Only test characters that actually exist in s

        for c in char_set:
            count = 0  # How many times target character `c` appears in window
            l = 0

            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                # Window size is (r - l + 1).
                # Replacements needed to turn the entire window into `c`:
                # (window_size) - count
                while (r - l + 1) - count > k:
                    # Too many replacements needed, shrink from the left
                    if s[l] == c:
                        count -= 1
                    l += 1

                # If we are here, at most k replacements are needed:
                res = max(res, r - l + 1)

        return res