class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_map = {}
        majority = 0
        res = 0
        for i in range(len(nums)):
            nums_map[nums[i]] = 1 + nums_map.get(nums[i],0)
            if nums_map[nums[i]] > majority:
                res = nums[i]
                majority = nums_map[nums[i]]
        return res
