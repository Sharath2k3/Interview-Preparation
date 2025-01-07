class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left,count =0,0
        for i in range(len(nums)-1):
            left = left + nums[i] 
            right = total - left
            if left>=right:
                count+=1
        return count
