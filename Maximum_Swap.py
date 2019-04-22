import math


class Solution:

    _arr = []

    def _get_arr (self, num, arr):
        if num == 0:
            return
        return self._get_arr(int(num/10),arr), arr.append(num % 10)

    def _arr_to_num(self, arr) -> int:
        ret = 0
        len_ = arr.__len__()
        for i, v in enumerate(arr):
            ret = ret + math.pow(10, len_ - i-1)*v
        return int(ret)

    def _get_max_num(self, arr, pos) -> int:
        n = pos
        max_num = 0
        len_ = arr.__len__()
        idx = n
        while n < len_:
            if arr[n] >= max_num:
                max_num = arr[n]
                idx = n
            n = n + 1
        return max_num, idx

    def _swap(self, arr, pos1, pos2):
        num = arr[pos1]
        arr[pos1] = arr[pos2]
        arr[pos2] = num

    def _is_swap(self, arr, pos) -> bool:
        num = arr[pos]
        len_ = arr.__len__()
        n = pos
        while n < len_-1:
            max_num, i = self._get_max_num(arr, n+1)
            if max_num > num:
                self._swap(arr, pos, i)
                return True
            n = n + 1
        return False

    def maximumSwap(self, num):
        self._arr = []
        self._get_arr(num,self._arr)
        for i in range(self._arr.__len__()):
            if self._is_swap(self._arr, i):
                break
        return self._arr_to_num(self._arr)
