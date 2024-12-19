class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []

        def binary_search(res,n):
            left,right=0,len(res)-1
            while left<right:
                mid = left+right//2
                if res[mid]==n:
                    return mid
                if res[mid]>n:
                    right = mid-1
                else:
                    left=mid+1
            return left

        for i in nums:
            if not res or res[-1]<i:
                res.append(i)
            else:
                index = binary_search(res,i)
                res[index] = i

        return len(res)