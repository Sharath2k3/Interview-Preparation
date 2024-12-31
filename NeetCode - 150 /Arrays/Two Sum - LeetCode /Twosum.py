class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        num_map = {}
        for i in range(len(nums)):
            num_map[nums[i]] = i 
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_map and num_map[complement]!=i:
                return [i,num_map[complement]]
        
        return []