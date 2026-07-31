class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            rob1 = 0
            rob2 = 0

            for money in arr:
                newRob = max(rob1 + money, rob2)
                rob1 = rob2
                rob2 = newRob

            return rob2

        return max(helper(nums[:-1]), helper(nums[1:]))