class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left_total = 0

        for i in range(len(nums)):
            right_total = total - left_total - nums[i]

            if right_total == left_total:
                return i
            
            left_total += nums[i]

        return -1