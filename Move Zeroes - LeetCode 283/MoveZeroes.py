class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right]!=0:
                nums[left],nums[right] = nums[right],nums[left]
                left+=1
        return nums
