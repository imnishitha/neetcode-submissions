from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)     # required counts
        window = {}           # current window counts
        have = 0
        need_count = len(need)

        res = [-1, -1]
        res_len = float("inf")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            # try shrinking
            while have == need_count:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # pop from left
                left_char = s[l]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
