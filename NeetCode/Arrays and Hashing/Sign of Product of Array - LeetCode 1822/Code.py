class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pr = 1
        for num in nums:
            pr = pr * num
        if pr < 0:
            return -1
        elif pr==0:
            return 0
        else:
            return 1
