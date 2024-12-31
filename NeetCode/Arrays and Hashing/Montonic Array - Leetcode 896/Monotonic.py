class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n==1:
            return True
        
        isinc = True
        isdec = True

        for i in range(1,n):
            if not isinc and not isdec:
                return False
            
            if nums[i-1]> nums[i]:
                isinc = False
            
            if nums[i-1] < nums[i]:
                isdec = False

        return isinc or isdec