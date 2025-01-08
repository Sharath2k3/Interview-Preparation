class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        dp = []

        for num in nums:
            left = 0
            right = len(dp)-1

            while left<=right:
                mid = (left+right)//2
                if dp[mid]<num:
                    left = mid + 1
                else:
                    right = mid - 1
            
            if left == len(dp):
                dp.append(num)
            else:
                dp[left]=num
            
        return len(dp)