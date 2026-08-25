class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        result = n

        for i in range(n):
            result ^= i
            result ^= nums[i]

        return result