class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentsum = nums[0]
        maxsum = nums[0]

        for i in range(1,len(nums)):
            sum = currentsum+nums[i]
            currentsum = max(nums[i],sum)
            maxsum = max(currentsum,maxsum)
        
        return maxsum
        