class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=0
        arr=[]
        for i in range(len(nums)):
            s+=nums[i]
            arr.append(s)
        return arr