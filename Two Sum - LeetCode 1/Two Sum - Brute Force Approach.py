class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)#Finding the length of the array
        arr=[]#Final array
        for i in range(n):
            for j in range(i+1,n):
                if(nums[i]+nums[j]==target):
                    arr.append(i)
                    arr.append(j)
        return arr
                    