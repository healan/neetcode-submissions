class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long_str = ''
        long_len = 0
        cur_len = 0

        for char in s:
            if char not in long_str:
                long_str += char
                cur_len = len(long_str)

                long_len = max(long_len, cur_len)

            else:
                idx = long_str.index(char)
                long_str = long_str[idx+1:]+char


        return long_len