class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] =1 + hashmap.get(nums[i],0)
        index =0 
        for color in range(3):
            freq = hashmap.get(color,0)
            nums[index:index+freq] = [color] * freq
            index = index + freq
