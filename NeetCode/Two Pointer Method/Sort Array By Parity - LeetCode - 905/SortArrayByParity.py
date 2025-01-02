class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even_index = 0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i],nums[even_index] = nums[even_index],nums[i]
                even_index+=1
        
        return nums