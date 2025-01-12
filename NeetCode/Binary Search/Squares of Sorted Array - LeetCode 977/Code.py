class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = 0
        right = n-1

        res = [0] * n 
    
        for i in range(n-1,-1,-1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left+=1
            else:
                res[i] = nums[right] ** 2
                right-=1
        
        return res