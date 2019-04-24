import math
class Solution:
    def _construct_new_str(self, s: str) -> str:
        len_ = len(s)
        s_new = ['#']*(2*len_+1)
        for i, v in enumerate(s):
            s_new[2*i+1] = v
        return s_new

    def _palindrome_length(self, s: str, i: int) -> int:
        len_ = len(s)
        length = 0
        n = 0
        while i-n >= 0 and i+n < len_:
            if s[i-n] == s[i+n]:
                length = length + 1
                n = n + 1
            else:
                break
        return length-1

    def longestPalindrome(self, s: str) -> str:
        s_new = self._construct_new_str(s)
        max_len = 0
        pos = 0
        for i, v in enumerate(s_new):
            len_ = self._palindrome_length(s_new, i)
            if len_ > max_len:
                max_len = len_
                pos = (i-1)/2
        idx1 = pos + 0.5 - (max_len / 2)
        idx2 = pos-0.5+(max_len/2)
        return s[int(idx1):int(idx2)+1]