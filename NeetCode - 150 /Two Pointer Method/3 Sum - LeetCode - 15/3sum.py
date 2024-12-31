class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        s = set()
        output = []
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                sum = nums[i]+nums[j]+nums[k]
                if sum == 0:
                    s.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif sum < 0:
                    j+=1
                else:
                    k-=1
        output = list(s)
        return output
