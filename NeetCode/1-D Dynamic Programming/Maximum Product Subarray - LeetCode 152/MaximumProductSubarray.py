class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_min = nums[0]
        current_max = nums[0]
        max_product = nums[0]

        for num in nums[1:]:
            if num<0:
                current_min,current_max = current_max,current_min
            
            current_min = min(current_min*num,num)
            current_max = max(current_max*num,num)
            max_product = max(max_product,current_max)
        
        return max_product