class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        len_ = len(nums)
        max_num = [None]*len_
        max_num[0] = nums[0]    # max_num[i] is the sum of max subarray which ended with nums[i]
        i = 1
        while i < len_:
            if max_num[i-1] > 0:
                max_num[i] = max_num[i-1] + nums[i]
            else:
                max_num[i] = nums[i]
            i = i+1
        return max(max_num)